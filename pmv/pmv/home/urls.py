from . import views
from django.urls import path

app_name = 'home'

    

urlpatterns = [
    path('', views.home, name ='home'  ),
    path('technical-specifications/', views.specs, name ='specs'  ),
    path('career/', views.career_form, name ='career'  ),
    path('form_submit/', views.career_confirm, name ='career_confirm'  ),

]