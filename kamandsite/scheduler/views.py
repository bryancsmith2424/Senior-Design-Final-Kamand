from django.shortcuts import render
from django.urls import reverse


from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import timedelta, datetime

from .models import Profile, Course, Assignment


def index(request):
    return render(request, 'scheduler/index.html')

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
    except(KeyError):
        return render(request, 'scheduler/error.html')
    else:
        for course in class_name_list:
            if course != '':
                Course.objects.create(user=user, coursename=course)

        '''
        user.profile.class1 = class_name_list[0]
        user.profile.class2 = class_name_list[1]
        user.profile.class3 = class_name_list[2]
        user.profile.class4 = class_name_list[3]
        user.profile.class5 = class_name_list[4]
        user.profile.class6 = class_name_list[5]
        user.profile.class7 = class_name_list[6]
        '''


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
                deadline = datetime.fromisoformat(deadline)
                duration = timedelta(hours = float(duration))
                Assignment.objects.create(user=user, course=Course.objects.get(pk=course), assignment_type=type, assignment_name=name, deadline=deadline, time_to_complete_estimate=duration)
        except(KeyError):
            pass
    return HttpResponseRedirect(reverse('scheduler'))

def get_calendar_data(request):
    context = {'range': range(50)}
    return render(request, 'scheduler/quickstart.html', context)

def create_schedule(request):
    #context = request.POST
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

    return render(request, 'scheduler/create_schedule.html', context)
