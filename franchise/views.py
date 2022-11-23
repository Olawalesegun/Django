from django.shortcuts import render
from franchise.models import Customer, Products, Needs
from django.http import JsonResponse
# Create your views here.
def CustomerDetails(request):
    customer = Customer.objects.all()
    data = {
        'customers': list(customer.values())
    }
    return JsonResponse(data)