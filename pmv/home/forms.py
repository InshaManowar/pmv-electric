from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from home.models import CareerRequest, Dealer, Fleet, Interest, Order
from django.contrib.admin.widgets import AdminDateWidget


class CareerForm(forms.ModelForm):

    class Meta:
        model = CareerRequest
        fields = '__all__'
        labels ={
            'name':'',
            'email':'',
            'position':'',         
            'cover_letter':'',
            'phone':'',
            'interest':'Your Interest',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Name'}),
                                    'phone': forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone'}),

            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email'}),
            'position': forms.TextInput(attrs = {'class':'form-control','placeholder':'Position'}),
            'cover_letter': forms.Textarea(attrs = {'class':'form-control','placeholder':'Cover Letter'}),
        }

class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = '__all__'
        labels ={
            'name':'',
            'email':'',
            'message':'',
            'phone':'',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Name'}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email id'}),
                        'phone': forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone'}),

            'message': forms.Textarea(attrs = {'class':'form-control','placeholder':'Your message'}),
        }
class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = '__all__'
        labels ={
            'name':'',
            'email':'',
            'message':'',
            'phone':'',
            'pin_code':'',
            'location':'',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Name'}),
            'location': forms.TextInput(attrs = {'class':'form-control','placeholder':'Location'}),
            'phone': forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone'}),
            'pin_code': forms.TextInput(attrs = {'class':'form-control','placeholder':'Pin Code'}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email id'}),
                        'phone': forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone'}),

            'message': forms.Textarea(attrs = {'class':'form-control','placeholder':'Your message'}),
        }
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
     
        widgets = {
            'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Last Name'}),
            'company_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Company Name'}),
            'city': forms.TextInput(attrs = {'class':'form-control','placeholder':'City'}),
            'postcode': forms.TextInput(attrs = {'class':'form-control','placeholder':'Postal code/zip code'}),
            'phone': forms.TextInput(attrs = {'class':'form-control','placeholder':'Phone'}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email id'}),
            'order_notes': forms.Textarea(attrs = {'class':'form-control','placeholder':'Order notes (if any)'}),
        }
class FleetForm(forms.ModelForm):
    class Meta:
        model = Fleet
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Name'}),
            'company_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Company Name'}),
            'website': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Website'}),
            'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Phone'}),
            'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email'}),
            'message': forms.Textarea(attrs = {'class':'form-control','placeholder':'Message'}),
        }
        labels ={
            'name':'',
            'email':'',
            'message':'',
            'company_name':'',
            'website':'',
            'phone':'',
        }
class ContactForm(forms.Form):
    name = forms.CharField(max_length = 150)
    company = forms.CharField(max_length=200)
    email_address = forms.EmailField(max_length = 150)
    phone = forms.CharField(max_length=10)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000  )
    class Meta:
        fields = '__all__'
        labels ={
            'name':'',
            'email':'',
            'message':'',
            'company_name':'',
            'phone':'',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Name'}),
            'company_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Company Name'}),
            'phone': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Phone'}),
            'email_address': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Email'}),
            'message': forms.Textarea(attrs = {'class':'form-control','placeholder':'Message'}),
        }

        