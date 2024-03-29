from django.db import models
from enum import Enum
import random
import time
import logging
# Create your models here.
class Customer(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    def __str__(self):
    	return "email: " + self.email + " password (in clear text, of course): " + str(self.password)

class StatesClass (Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMEOUT = "TIMEOUT"
    IN_PROGRESS = "IN_PROGRESS"
    TO_DO = "TO_DO"

class Task(models.Model):
    ID = models.CharField(max_length=200, primary_key=True)
    state = models.CharField(
        max_length = 200,
        choices=[(tag.name, tag.value) for tag in StatesClass],
        default=StatesClass.TO_DO.value
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
        time.sleep(10) #simulate processing time
            
        
        