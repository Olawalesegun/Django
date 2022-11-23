from django.contrib import admin
from franchise.models import Customer, Products, Needs 

# Register your models here.
admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Needs)