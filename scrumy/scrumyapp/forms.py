from django import forms
from .models import ScrumyUser, ScrumyGoals

class AddUserForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta:

        model = ScrumyUser
        widgets = {'password1' : forms.PasswordInput(render_value=True), 'password2' : forms.PasswordInput(render_value=True)}

        fields = ['first_name','last_name','username','password1','password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password Dont match")
        return password2

    def save(self, commit=True):
        user = super(AddUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['status_id', 'task']
        #fields = '__all__'

class ChangeTaskStatusForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields=['status_id']