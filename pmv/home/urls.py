from . import views
from django.urls import path

app_name = 'home'

    

urlpatterns = [
    path('', views.home, name ='home'  ),
    path('technical-specifications/', views.specs, name ='specs'  ),
    path('career/', views.career_form, name ='career'  ),
    path('thanks/', views.career_confirm, name ='career_confirm'  ),
    path('gallery/', views.gallery, name ='gallery'  ),
    # path('video/', views.videos, name ='video'  ),
    path('contact/', views.contact_form, name ='contact'  ),
    path('dealership-enquiry/', views.dealer_form, name ='dealer'  ),
    path('express-interest/', views.interest_form, name ='interest'  ),
    path('products/', views.products, name ='products'  ),
    path('products/detail/', views.product_detail, name ='products_detail'  ),
    path('our-mission/', views.mission, name ='mission'  ),
    path('fleet-request/', views.fleet_form, name ='fleet'  ),
    path('frequently-asked-questions/', views.faqs, name ='faqs'  ),
    path('watch-out/', views.watchout, name ='watchout'  ),

]