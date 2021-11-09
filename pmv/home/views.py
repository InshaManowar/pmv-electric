from django.shortcuts import render, redirect
from home.forms import CareerForm, DealerForm, ContactForm
from .models import CareerRequest,Photos, Video, Faqs
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render (request, 'home/home.html')

def products(request):
    return render (request, 'home/product.html')

def specs(request):
    return render (request, 'home/specs.html')

def career_form(request):
    form = CareerForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home:career_confirm')
    context = {'form':form}
        
    return render(request, 'home/career.html', context)


def dealer_form(request):
    form_dealer = DealerForm()
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home:dealer')
    context = {'form_dealer':form_dealer}
    return render(request, 'home/dealer.html', context)


def career_confirm(request):
    return render(request, 'home/career_confirm.html')

def photos(request):
    photo = Photos.objects.all()
    return render(request, 'home/gallery.html', {'photo':photo})

def videos(request):
    display = Video.objects.all()
    return render(request, 'home/gallery.html', {'display':display})

def faqs(request):
    faq = Faqs.objects.all()
    return render(request, 'home/faq.html', {'faq':faq})


def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Subject Inquiry"

            body = {
                'name': form.cleaned_data['name'], 
			    'company': form.cleaned_data['company'], 
			    'email': form.cleaned_data['email_address'], 
			    'message':form.cleaned_data['message'], 
			    'phone':form.cleaned_data['phone'], 
                }

            message = "\n".join(body.values())
            recepient = str(form['email_address'].value())
            
            try:
                send_mail(subject, message, recepient, ['sociio.organisation@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("home:home")
    
    form = ContactForm(request.POST)
    return render(request, "home/home.html", {'contact_form':form})

