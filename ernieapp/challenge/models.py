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
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    IN_PROGRESS = "IN_PROGRESS"
    TO_DO = "TO_DO"

class Task(models.Model):
    ID = models.IntegerField(max_length=200, primary_key=True)
    state = models.CharField(
        max_length = 5,
        choices=[(tag, tag.value) for tag in States],
        default=States.TO_DO.value
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
