from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'scheduler/index.html')

def start(request):
    return render(request, 'scheduler/start.html')
