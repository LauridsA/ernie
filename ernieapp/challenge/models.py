from django.db import models
from enum import Enum
# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    #LIST DEVICES
    #LIST TASKS
    def __str__(self):
    	return "email: " + self.email + " password (in clear text, of course): " + str(self.password) + str(self.rank)

class States(Enum):
    SUCCESS = 1
    FAILED = 2
    TIMEOUT = 3
    IN_PROGRESS = 4
    TO_DO = 5

class Task(models.Model):
    ID = models.IntegerField(max_length=200, primary_key=True)
    state = models.IntegerField(
        max_length = 6,
        choices=[(tag, tag.value) for tag in States],
        default=States.TO_DO
    ) 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
    	return "ID: " + str(self.ID) + " with state: " + str(self.state)

class Device(models.Model):
    UUID = models.CharField(max_length=200, primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
    	return "ID: " + str(self.UUID)
    def execute(self):
        return "execute function invoked"
