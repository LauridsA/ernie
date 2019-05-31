from django.db import models

# Create your models here.

class Task(models.Model):
    ID = models.IntegerField(max_length=200, primary_key=True)
    #constants
    SUCCESS = 1
    FAILED = 2
    TIMEOUT = 3
    IN_PROGRESS = 4
    TO_DO = 5
    state_choices = [
        (SUCCESS, 1),
        (FAILED, 2),
        (TIMEOUT, 3),
        (IN_PROGRESS, 4),
        (TO_DO, 5)
    ]
    #state
    state = models.IntegerField(
        max_length = 1,
        choices=state_choices,
        default=TO_DO
    ) 
    def __str__(self):
    	return "ID: " + str(self.ID) + " with state: " + str(self.state)

class Device(models.Model):
    UUID = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
    	return "ID: " + str(self.UUID)
    def execute(self):
        return ""

class Customer(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    #LIST DEVICES
    #LIST TASKS
    def __str__(self):
    	return "email: " + self.email + " password (in clear text, of course): " + str(self.password) + str(self.rank)