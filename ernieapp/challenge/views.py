from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Task, Customer
import requests as req
# Create your views here.

def index(request):
	deviceList = Device.objects.all()
	return HttpResponse(deviceList)


def TasksInDevice(request, UUID):
    tasks = Task.objects.filter(customer__device__UUID=UUID)
    # get tasks based on customer and list where customer.id == device.customer.id
    return HttpResponse(tasks)

def notifyNewTask(request, ID):

    return HttpResponse("what")

def notifyTaskResult(request, ID):

    return HttpResponse("also what")