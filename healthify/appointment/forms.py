from django import forms
from .models import Appointment

time_choices  = [
    ('-----','-----'),
    ('9AM-12PM','9AM-12PM'),
    ('3PM-6PM','3PM-6PM'),

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

class AppointmentForm(forms.ModelForm):
    Appointment_Date = forms.DateField(widget=forms.DateInput(attrs = {'type':'date'}))
    Appointment_Time = forms.ChoiceField(choices = time_choices )
    Blood_Group = forms.ChoiceField(choices =Blood_Group  )

    class Meta:
        model = Appointment
        fields = '__all__'
