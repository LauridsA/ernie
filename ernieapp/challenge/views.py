from django.shortcuts import render
from django.http import HttpResponse
from .models import Device, Task, Customer, StatesClass
import requests as req
import random
# Create your views here.

def index(request):
    #deviceList = Device.objects.filter(Customer=)
    return HttpResponse("Endpoints are: /TaskResult/ID, /TasksInDevice/UUID, /TaskStarted/ID, /RunTaskInDevice/UUID")


def TasksInDevice(request, UUID):
    # get tasks based on customer and list where UUID = customer.device.UUID
    tasks = Task.objects.filter(customer__device__UUID=UUID)
    return HttpResponse(tasks)

def notifyNewTask(request, ID):
    # get the related task/device combination for prettyness
    dev = Device.objects.filter(customer__task__ID=ID)
    return HttpResponse("Task with ID: " + ID + " has begun. It was picked up by device with ID: " + dev.UUID)

def notifyTaskResult(request, ID):
    task = Task.objects.get(ID=ID)
    return HttpResponse("Task with ID: " + ID + " changed state to: " + task.state)

def RunTaskInDevice(request, UUID):
    #this query could be optimized
    dev = Device.objects.select_related().get(UUID=UUID)
    taskList = Task.objects.filter(customer__email=dev.customer.email, state=StatesClass.TO_DO.value)
    if len(taskList) > 0:
        #call new task endpoint
        randomNum = random.randint(0,2) # simulate possibility of timeout (50-50 chance)
        task = taskList[0]
        task.state = StatesClass.IN_PROGRESS.value
        task.save()
        dev.execute()
        if(randomNum > 1): #timeout
            task.state = StatesClass.TIMEOUT.value
            task.save()
        else: #success
            task.state = StatesClass.SUCCESS.value
            task.save()
    #call endpoint task result
    return HttpResponse(dev)