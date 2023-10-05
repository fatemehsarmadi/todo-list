from django import forms
from .models import Task
from .widgets import DatePickerInput

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

class DeadlineForm(forms.Form):
    date = forms.DateField(widget=DatePickerInput)
    description = forms.CharField(max_length=30)
    priority = forms.IntegerField()
    task = forms.ModelChoiceField(queryset=Task.objects.all(), required=False, widget=forms.HiddenInput())
