
from django.db import models
#from django.contrib.auth.models import AbstractUser
#from django.utils.html import escape, mark_safe
#from django.contrib.auth import get_user_model
#from django.forms import PasswordInput

class ToDoList(models.Model):
    name = models.CharField(max_length=255)
   

    def __str__(self):
        return self.name




class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.TextField()
    complete = models.BooleanField()
    



    def __str__(self):
        return self.text
