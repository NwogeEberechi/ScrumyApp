from django import forms
from .models import ScrumyUser

class AddUserForm(forms.ModelForm):
    class Meta:
        model = ScrumyUser
        #fields = ['firstname', 'lastname', 'email', 'password', 'role']
        fields = '__all__'