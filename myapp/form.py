from django import forms
from .models import task

class taskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title','desc','time']

