from django.shortcuts import render, redirect
from home.forms import CareerForm, DealerForm, ContactForm,FleetForm, InterestForm, OrderForm
from .models import CareerRequest,Photos, Item
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render (request, 'home/home.html')
def products(request):
    return render (request, 'home/product.html')
def product_detail(request):
    return render (request, 'home/product_detail.html')
def mission(request):
    return render (request, 'home/missions.html')
def watchout(request):
    return render (request, 'home/watchout.html')
def specs(request):
    return render (request, 'home/specs.html')
def reserver_car(request):
    return render (request, 'home/shop/index.html')

def career_form(request):
    form = CareerForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Career Request'
            message = "You have received a new career request"
            recipient = str(form['email'].value())
            
            try:
                send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form':form}
    return render(request, 'home/career.html', context)


def dealer_form(request):
    form_dealer = DealerForm()
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Dealer Enquiry '
            body = {
                'name': form_dealer.cleaned_data['name'], 
			    'email': form_dealer.cleaned_data['email'], 
			    'phone':form_dealer.cleaned_data['phone'], 
                'message':form_dealer.cleaned_data['message'], 
                }
            message = "\n".join(body.values())
            recepient = str(form['email'].value())
            
            try:
                send_mail(subject, message, recepient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form_dealer':form_dealer}
    return render(request, 'home/dealer.html', context)


def fleet_form(request):
    form_fleet = FleetForm()
    if request.method == 'POST':
        form_fleet = FleetForm(request.POST)
        if form_fleet.is_valid():
            form_fleet.save()
            subject = 'fleet enquiry '
            
            body = {
                'name': form_fleet.cleaned_data['name'], 
			    'email': form_fleet.cleaned_data['email'], 
			    'website':form_fleet.cleaned_data['website'], 
			    'phone':form_fleet.cleaned_data['phone'], 
                'message':form_fleet.cleaned_data['message'], 
                }
            message = "\n".join(body.values())

            recipient = str(form_fleet['email'].value())
            
            try:
                send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form_fleet':form_fleet}
    return render(request, 'home/fleet.html', context)

def interest_form(request):
    form_interest = InterestForm()
    if request.method == 'POST':
        form_interest = InterestForm(request.POST)
        if form_interest.is_valid():
            form_interest.save()
            subject = 'Someone expressed interest!'
            body = {
                'name': form_interest.cleaned_data['name'], 
			    'email': form_interest.cleaned_data['email'], 
			    'location': form_interest.cleaned_data['location'], 
			    'pin_code': form_interest.cleaned_data['pin_code'], 
			    'phone':form_interest.cleaned_data['phone'], 
                'message':form_interest.cleaned_data['message'], 
                }
            message = "\n".join(body.values())
        
            recipient = str(form_interest['email'].value())
            try:
                send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form_interest':form_interest}
    return render(request, 'home/interest.html', context)


def contact_form(request):
    form_contact = ContactForm()
    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            subject = 'Someone expressed interest!'
            body = {
                'name': form_contact.cleaned_data['name'], 
			    'email': form_contact.cleaned_data['email'], 
                'message':form_contact.cleaned_data['message'], 
                'subject':form_contact.cleaned_data['subject'], 
                }
            message = "\n".join(body.values())
        
            recipient = str(form_contact['email'].value())
            try:
                send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form_contact':form_contact}
    return render(request, 'home/contact.html', context)


def contact_form_home(request):
    form_contact = ContactForm()
    if request.method == 'POST':
        form_contact = ContactForm(request.POST)
        if form_contact.is_valid():
            form_contact.save()
            subject = 'Someone expressed interest!'
            body = {
                'name': form_contact.cleaned_data['name'], 
			    'email': form_contact.cleaned_data['email'], 
                'message':form_contact.cleaned_data['message'], 
                'subject':form_contact.cleaned_data['subject'], 
                }
            message = "\n".join(body.values())
        
            recipient = str(form_contact['email'].value())
            try:
                send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form_contact':form_contact}
    return render(request, 'home/home.html', context)


def career_confirm(request):
    return render(request, 'home/career_confirm.html')


def faqs(request):
    return render(request, 'home/faq.html')

def gallery(request):
    photo = Photos.objects.all()
    obj = Item.objects.all()
    return render(request, 'home/gallery.html', {'photo':photo, 'obj':obj})


# def contactus(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST or None)
#         if form.is_valid():
#             subject = "Subject Inquiry"

#             body = {
#                 'name': form.cleaned_data['name'], 
# 			    'company': form.cleaned_data['company'], 
# 			    'email': form.cleaned_data['email_address'], 
# 			    'message':form.cleaned_data['message'], 
# 			    'phone':form.cleaned_data['phone'], 
#                 }

#             message = "\n".join(body.values())
#             recipient = str(form['email_address'].value())
            
#             try:
#                 send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect ("home:home")
    
#     form = ContactForm(request.POST or None)
#     return render(request, "home/home.html", {'contact_form':form})



def order_form(request):
    form_order = OrderForm()
    if request.method == 'POST':
        form_order = OrderForm(request.POST)
        if form_order.is_valid():
            form_order.save()
            subject = 'You have a new order'
            body = {
                'first_name': form_order.cleaned_data['first_name'], 
                'last_name': form_order.cleaned_data['last_name'], 
                'company_name': form_order.cleaned_data['company_name'], 
			    'email': form_order.cleaned_data['email'], 
			    'country': form_order.cleaned_data['country'], 
			    'state': form_order.cleaned_data['state'], 
			    'city': form_order.cleaned_data['city'], 
			    'postcode': form_order.cleaned_data['postcode'], 
			    'phone':form_order.cleaned_data['phone'], 
                'order_notes':form_order.cleaned_data['order_notes'], 
                }
            message = "\n".join(body.values())
        
            recipient = str(form_order['email'].value())
            
            try:
                send_mail(subject, message, recipient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ('home:career_confirm')
    context = {'form_order':form_order}
    return render(request, 'home/checkout.html', context)

