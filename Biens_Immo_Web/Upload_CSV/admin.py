from django.contrib import admin
from .models import Immo, Contact


# Register your models here.

@admin.register(Immo)
class RequestImmo(admin.ModelAdmin):
    list_display = [field.name for field in Immo._meta.get_fields()]
    search_fields = ['departement']

@admin.register(Contact)
class RequestContact(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]
