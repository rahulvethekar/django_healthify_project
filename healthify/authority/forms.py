from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor,Nurse,RoomService

class AdminRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


Speciality = [
    ('Neurologists','Neurologists'),
    ('Family Physicians','Family Physicians'),
    ('Cardiologists','Cardiologists'),
    ('Plastic Surgeons','Plastic Surgeons'),
    ('Infectious Disease Specialists','Infectious Disease Specialists'),
    ('Eye Specialist','Eye specialist'),
    ('Dental Specialist','Dental Specialist'),

]

Shift = [
    ('Morning','Morning'),
    ('Afternoon','Afternoon'),
    ('Night','Night'),

]

department = [
    ('OPD','OPD'),
    ('ICU','ICU'),
    ('General','General'),
    ('Operation Theater','Operation theater'),


]


class DoctorModelForm(forms.ModelForm):
    Speciality = forms.ChoiceField(choices=Speciality)

    class Meta:
        model = Doctor
        fields = '__all__'


class NurseModelForm(forms.ModelForm):

    Department = forms.ChoiceField(choices = department)
    Shift = forms.ChoiceField(choices = Shift)


    class Meta:
        model = Nurse
        fields = '__all__'


class RoomServiceModelForm(forms.ModelForm):

    class Meta:
        fields = '__all__'



