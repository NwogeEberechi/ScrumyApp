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
        fields = ['user_id', 'status_id', 'task']
        #fields = '__all__'

class ChangeTaskStatusForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields=['status_id']