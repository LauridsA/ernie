from django.contrib import admin

# Register your models here.
from .models import Device, Task, Customer

admin.site.register(Customer)
admin.site.register(Task)
admin.site.register(Device)