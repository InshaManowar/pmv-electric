from . import views
from django.urls import path

app_name = 'home'

    

urlpatterns = [
    path('', views.home, name ='home'  ),
    path('technical-specifications/', views.specs, name ='specs'  ),
    path('career/', views.career_form, name ='career'  ),
    path('career/thanks/', views.career_confirm, name ='career_confirm'  ),
    path('gallery/', views.photos, name ='gallery'  ),
    path('contact/', views.contactus, name ='contact'  ),
    path('dealership-enquiry/', views.dealer_form, name ='dealer'  ),
    path('products/', views.products, name ='products'  ),
    path('products/detail/', views.product_detail, name ='products_detail'  ),
    path('our-mission/', views.mission, name ='mission'  ),
    path('fleet-request/', views.fleet_form, name ='fleet'  ),
    path('frequently-asked-questions/', views.faqs, name ='faqs'  ),
    path('watch-out/', views.watchout, name ='watchout'  ),

]