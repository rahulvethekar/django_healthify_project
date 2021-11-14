from django import forms
from .models import Ambulance

reasons = [
    ('Road accident','Road accident'),
    ('Cardio arrest ','Cardio arrest'),
    ('Childbirth','Childbirth'),
    ('Any other','Any other'),
]

class AmbulanceModelForm(forms.ModelForm):
    Reason = forms.ChoiceField(choices =reasons)
    class Meta:
        model = Ambulance
        fields = '__all__'