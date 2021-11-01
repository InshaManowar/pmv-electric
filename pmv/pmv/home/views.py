from django.shortcuts import render, redirect
from home.forms import CareerForm
from .models import CareerRequest

# Create your views here.
def home(request):
    return render (request, 'home/home.html')

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

def career_confirm(request):
    return render(request, 'home/career_confirm.html')
