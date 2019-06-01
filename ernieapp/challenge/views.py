from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Task
import requests as req
# Create your views here.

def index(request):
	deviceList = Device.objects.all()
	return HttpResponse(deviceList)


def TasksInDevice(request, UUID):
    dev = Device.objects.filter(UUID=UUID)
    return HttpResponse("TasksInDevice")

def notifyNewTask(request, ID):

    return HttpResponse("what")

def notifyTaskResult(request, ID):

    return HttpResponse("also what")