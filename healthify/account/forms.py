from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PersonalInfo

Gender = [
    ('Male','Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),

]
Blood_Group = [
    ('-------','-------'),
    ('A+','A+'),
    ('O+', 'O+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('A-', 'A-'),
    ('O-', 'O-'),
    ('B+', 'B+'),
    ('AB-', 'AB-'),

]



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')


class PersonalInfoForm(forms.ModelForm):
    Gender = forms.ChoiceField(choices = Gender , widget = forms.RadioSelect)
    Blood_Group = forms.ChoiceField( choices = Blood_Group)
    class Meta:
        model = PersonalInfo
        fields = '__all__'
