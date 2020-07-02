from django import forms
from django.forms import ModelForm
import datetime

class feedbackForm(forms.Form):
    CHOICES =[('agro','Agro'),
         ('edu','Education'),
         ('med', 'Medical'),
         ('trans', 'Transport/Admin')]
    lat = forms.DecimalField(label= "Latitude", disabled=True)
    lng = forms.DecimalField(label = "Longitude",disabled=True)
    address = forms.CharField(required=True)
    #date = forms.DateField() #hidden field
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    pin = forms.DecimalField(required=True)
    domain = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    date = forms.DateField(initial = datetime.date.today, widget=forms.HiddenInput())

"""class FeedbackForm1(ModelForm):
        class Meta:
            model = FeedbackModel
            fields = ['lat', 'lng', 'address', 'city', 'state', 'pin', 'domain', 'date']
            """