from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from home.models import CareerRequest, Dealer, Fleet
from django.contrib.admin.widgets import AdminDateWidget

class CareerForm(forms.ModelForm):

    class Meta:
        model = CareerRequest
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput(attrs = {'class':'form-control'}),
            'position': forms.TextInput(attrs = {'class':'form-control'}),
            'cover_letter': forms.Textarea(attrs = {'class':'form-control'}),
        }

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput(attrs = {'class':'form-control'}),
            'message': forms.Textarea(attrs = {'class':'form-control'}),
        }
class FleetForm(forms.ModelForm):
    class Meta:
        model = Fleet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput(attrs = {'class':'form-control'}),
            'message': forms.Textarea(attrs = {'class':'form-control'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 150)
    company = forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length = 150)
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

        