from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from home.models import CareerRequest
from django.contrib.admin.widgets import AdminDateWidget

class CareerForm(forms.ModelForm):

    class Meta:
        model = CareerRequest
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control'}),
            'phone': forms.TextInput(attrs = {'class':'form-control'}),
            'email': forms.EmailInput(attrs = {'class':'form-control'}),
            'position': forms.TextInput(attrs = {'class':'form-control'}),
            'cover_letter': forms.Textarea(attrs = {'class':'form-control'}),
        }