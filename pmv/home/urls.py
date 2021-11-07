from . import views
from django.urls import path

app_name = 'home'

    

urlpatterns = [
    path('', views.home, name ='home'  ),
    path('technical-specifications/', views.specs, name ='specs'  ),
    path('career/', views.career_form, name ='career'  ),
    path('career/thanks/', views.career_confirm, name ='career_confirm'  ),
    path('gallery/', views.photos, name ='gallery'  ),
    path('dealership-enquiry/', views.dealer_form, name ='dealer'  ),
    path('frequently-asked-questions/', views.faqs, name ='faqs'  ),

]