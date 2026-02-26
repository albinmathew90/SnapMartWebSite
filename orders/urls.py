from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-order/', views.create_order, name='create_order'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path('invoice/<int:order_id>/', views.download_invoice, name='download_invoice'),
    path('register/', views.register, name='register'),
    
   
    
]