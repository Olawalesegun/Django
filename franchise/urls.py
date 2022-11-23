from django.urls import path
from franchise.views import CustomerDetails

urlpatterns = [
    path('customer/', CustomerDetails, name='index')
]