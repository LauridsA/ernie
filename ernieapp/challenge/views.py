from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Task
import requests as req
# Create your views here.

def index(request):
	return HttpResponse("coolindexpage")


def TasksInDevice(request, deviceID):
	return HttpResponse("TasksInDevice")

def notifyNewTask(request, deviceID):

    return HttpResponse("what")

def notifyTaskResult(request, deviceID):

    return HttpResponse("also what")