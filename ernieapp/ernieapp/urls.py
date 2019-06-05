"""ernieapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
sys.path.append('/challenge')
from django.contrib import admin
from django.urls import path
from challenge.models import Device, Task
from challenge.views import TasksInDevice, notifyNewTask, notifyTaskResult, index, RunTaskInDevice

urlpatterns = [
    path('', index, name="index"),
    path('TasksInDevice/<slug:UUID>', TasksInDevice, name="TasksInDeviceByUUID"),
    path('TaskResult/<slug:ID>', notifyTaskResult, name="ResultOfTaskByUUIDAndTaskID"),
    path('TaskStarted/<slug: ID>', notifyNewTask, name="NotificationOfNewStartedTask"),
    path('RunTaskInDevice/<slug: UUID>', RunTaskInDevice, name="ExecuteTask"),
    path('admin/', admin.site.urls),
]
