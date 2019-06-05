from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Task, Customer
import requests as req
# Create your views here.

def index(request):
    #deviceList = Device.objects.filter(Customer=)
    return HttpResponse("Endpoints are: /TaskResult/ID, /TasksInDevice/UUID, /TaskStarted/ID, /RunTaskInDevice/UUID")


def TasksInDevice(request, UUID):
    # get tasks based on customer and list where UUID = customer.device.UUID
    tasks = Task.objects.filter(customer__device__UUID=UUID)
    return HttpResponse(tasks)

def RunTaskInDevice(request, UUID):
    device = Device.objects.get(UUID=UUID)
    device.execute()
    return HttpResponse(device)

def notifyNewTask(request, ID):
    # get the related task/device combination for prettyness
    dev = Device.objects.filter(customer__task__ID=ID)
    return HttpResponse("Task with ID: " + ID + " has begun. It was picked up by device with ID: " + dev.UUID)

def notifyTaskResult(request, ID):
    task = Task.objects.get(ID=ID)
    return HttpResponse("Task with ID: " + ID + " changed state to: " + task.state)