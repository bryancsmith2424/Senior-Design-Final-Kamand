from django.shortcuts import render
from django.urls import reverse


from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login, logout

from datetime import timedelta, datetime, time, date, tzinfo

from pytz import timezone

from .models import Profile, Course, Assignment

from scheduler.modules.GreedyAlgo import greedyAlgo
from scheduler.modules.OptimalEvent import OptimalEvent
from scheduler.modules.Event import Event
from scheduler.modules.FindAvailableTime import findAvailableTime
from scheduler.modules.CreateOptimalEvents import createOptimalEvents

def index(request):
    return render(request, 'scheduler/index.html')

def pagelogout(request):
    if request.method == "POST":
        logout(request)

        return HttpResponseRedirect(reverse('scheduler'))

@login_required(login_url='/scheduler/')
def start(request):
    context = {'course_name_list': request.user.course_set.all(), 'course_name_count': request.user.course_set.count()}
    return render(request, 'scheduler/start.html', context)

@login_required(login_url='/scheduler/')
def goals(request):
    # user = User.objects.get(pk=user_id)
    return render(request, 'scheduler/goals.html')

@login_required(login_url='/scheduler/')
def update_goals(request):
    # user = User.objects.get(pk=user_id)
    user = request.user
    try:
        class_name_list = request.POST.getlist('class')
        start_time = time.fromisoformat(request.POST.get('start_time'))
        end_time = time.fromisoformat(request.POST.get('end_time'))
        productive_time = request.POST.get('productive_time')
    except(KeyError):
        return render(request, 'scheduler/error.html')
    else:
        user.profile.productive_time = productive_time
        user.profile.day_start_offset = int(start_time.hour - 9) + 1
        user.profile.day_end_offset = int(end_time.hour - 22)
        user.save()
        for course in class_name_list:
            if course != '':
                Course.objects.create(user=user, coursename=course)

        #context = {'user': user, 'user_id': user_id}
        return HttpResponseRedirect(reverse('scheduler'))

@login_required(login_url='/scheduler/')
def assignments(request):
    context = {'course_name_list': request.user.course_set.all(), 'course_name_count': request.user.course_set.count()}
    return render(request, 'scheduler/assignments.html', context)

@login_required(login_url='/scheduler/')
def update_assignments(request):
    user = request.user

    form_dict = request.POST

    for i in range(1, 10):
        try:
            course = form_dict.get("course{}".format(i))
            type = form_dict.get("type{}".format(i))
            name = form_dict.get("name{}".format(i))
            deadline = form_dict.get("deadline{}".format(i))
            duration = form_dict.get("duration{}".format(i))

            if (name == '') or (deadline == '') or (duration == ''):
                pass
            else:
                user_timezone = timezone(user.profile.timezone)
                deadline = user_timezone.localize(datetime.fromisoformat(deadline))
                duration = float(duration)
                Assignment.objects.create(user=user, course=Course.objects.get(pk=course), assignment_type=type, assignment_name=name, deadline=deadline, time_to_complete_estimate=duration)
        except(KeyError):
            pass
    return HttpResponseRedirect(reverse('scheduler'))

@login_required(login_url='/scheduler/')
def profile(request):
    today = datetime.today()
    context = {
        'course_name_list': request.user.course_set.all(),
        'course_name_count': request.user.course_set.count(),
        'assignment_list': request.user.assignment_set.filter(deadline__gte=today).order_by('deadline'),
    }
    return render(request, 'scheduler/profile.html', context)

@login_required(login_url='/scheduler/')
def edit_courses(request):
    today = datetime.today()
    context = {'course_list': request.user.course_set.all(),}
    return render(request, 'scheduler/edit/courses.html', context)

@login_required(login_url='/scheduler/')
def delete_courses(request):
    user = request.user
    form_dict = request.POST.copy()
    del form_dict['csrfmiddlewaretoken']
    for course_id in form_dict.values():
        try:
            user.course_set.filter(id=course_id).delete()
        except(KeyError):
            pass
    return HttpResponseRedirect(reverse('scheduler/start'))

@login_required(login_url='/scheduler/')
def edit_assignments(request):
    today = datetime.today()
    context = {'assignment_list': request.user.assignment_set.filter(deadline__gte=today).order_by('deadline'),}
    return render(request, 'scheduler/edit/assignments.html', context)

@login_required(login_url='/scheduler/')
def delete_assignments(request):
    user = request.user
    form_dict = request.POST.copy()
    del form_dict['csrfmiddlewaretoken']
    for assignment_id in form_dict.values():
        try:
            user.assignment_set.filter(id=assignment_id).delete()
        except(KeyError):
            pass
    return HttpResponseRedirect(reverse('scheduler/start'))


@login_required(login_url='/scheduler/')
def get_calendar_data(request):
    context = {'range': range(100)}
    return render(request, 'scheduler/get_schedule.html', context)

@login_required(login_url='/scheduler/')
def create_schedule(request):
    user = request.user
    '''
    context = {
    'eventList': [{
     'summary': 'Kamand Test event',
     'location': 'Busch?',
     'description': 'enetering an event via javascript',
     'start': {
       'dateTime': '2020-09-10T18:00:00',
       'timeZone': 'America/New_York',
     },
     'end': {
       'dateTime': '2020-09-10T19:00:00',
       'timeZone': 'America/New_York',
     },
     'attendees': [
       {'email': 'mpardonner@gmail.com'},
       {'email': 'enilnoswerdna@gmail.com'}
     ],
     'reminders': {
       'useDefault': True,
       },
    },]
    }
    '''
    form_dict = request.POST.copy()
    del form_dict['csrfmiddlewaretoken']
    event_dict_list = {'items': []}
    for i in range(100):
        if (len(form_dict.get('event_start{}'.format(i))) > 1):
            event_start = datetime.fromisoformat(form_dict.get('event_start{}'.format(i)))
            event_end = datetime.fromisoformat(form_dict.get('event_end{}'.format(i)))
            event = Event(event_start, event_end, "N/A", "N/A")
            event_dict = event.createDict()
            event_dict_list['items'].append(event_dict)
    avalible_times = findAvailableTime(event_dict_list, date.today() + timedelta(days = 1), date.today() + timedelta(days = 15), user.profile.day_start_offset, user.profile.day_end_offset, -4)
    assignment_list = user.assignment_set.filter(scheduled=False).filter(deadline__gte=date.today()).filter(deadline__lte=date.today()+timedelta(days=14)).order_by('deadline')
    if len(assignment_list) > 0:
        for assignment in assignment_list:
            assignment.scheduled = True
            assignment.save()
    tzinfo = timezone(user.profile.timezone)
    events_to_add = createOptimalEvents(assignment_list, user.profile.productive_time, tzinfo)
    event_schedule = greedyAlgo(avalible_times, events_to_add)
    event_dict_list = []
    for event in event_schedule:
        event_dict = event.createDict()
        event_dict_list.append(event_dict)
    context = {'eventList': event_dict_list}
    #x = foo


    return render(request, 'scheduler/create_schedule.html', context)
