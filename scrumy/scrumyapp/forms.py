from django import forms
from .models import ScrumyUser, ScrumyGoals

class AddUserForm(forms.ModelForm):
    class Meta:
        model = ScrumyUser
        #fields = ['firstname', 'lastname', 'email', 'password', 'role']
        fields = '__all__'

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = '__all__'