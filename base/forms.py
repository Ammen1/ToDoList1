
from django import forms
from.models import ToDoList,Item

class CreatNewList(forms.Form):
    name = forms.CharField(label="Name",max_length=200)
    check = forms.BooleanField(required=False)

 