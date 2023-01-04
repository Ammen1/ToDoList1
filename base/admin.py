from django.contrib import admin
from .models import Item, ToDoList

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
