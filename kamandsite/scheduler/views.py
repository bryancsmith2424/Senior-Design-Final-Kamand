from django.shortcuts import render
from django.urls import reverse


from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request, 'scheduler/index.html')

@login_required(login_url='/scheduler/')
def start(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {'user': user}
    return render(request, 'scheduler/start.html', context)

@login_required(login_url='/scheduler/')
def goals(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {'user': user, 'user_id': user_id}
    return render(request, 'scheduler/goals.html', context)

@login_required(login_url='/scheduler/')
def update_goals(request, user_id):
    user = User.objects.get(pk=user_id)
    try:
        class_name_list = request.POST.getlist('class')
    except(KeyError):
        return render(request, 'scheduler/error.html')
    else:
        user.profile.class1 = class_name_list[0]
        user.profile.class2 = class_name_list[1]
        user.profile.class3 = class_name_list[2]
        user.profile.class4 = class_name_list[3]
        user.profile.class5 = class_name_list[4]
        user.profile.class6 = class_name_list[5]
        user.profile.class7 = class_name_list[6]
        user.save()
        context = {'user': user, 'user_id': user_id}
        return HttpResponseRedirect(reverse('scheduler'))
