from django import forms
from project.models import Project, Task
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text='ex: Moodle 2 offline quiz editor ')
    description = forms.Textarea()

    class Meta:
        model = Project

class TaskForm(forms.ModelForm):
    summery = forms.CharField(max_length=200, help_text="Ex: Create UI")
    description = forms.Textarea()
    deadline = forms.DateTimeField()

    class Meta:
        model = Task

        fields = ('summery', 'description', 'deadline')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password')