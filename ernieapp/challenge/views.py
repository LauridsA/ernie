from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Task, Customer
import requests as req
# Create your views here.

def index(request):
	deviceList = Device.objects.all()
	return HttpResponse(deviceList)


def TasksInDevice(request, UUID):
    # get tasks based on customer and list where UUID = customer.device.UUID
    tasks = Task.objects.filter(customer__device__UUID=UUID)
    return HttpResponse(tasks)

def notifyNewTask(request, ID):
    # get the related task/device combination for prettyness
    #do the thing here
    dev = Device.objects.filter(customer__task__ID=ID)
    return HttpResponse("Task with ID: " + ID + " has begun.")

def notifyTaskResult(request, ID):

    return HttpResponse("also what")