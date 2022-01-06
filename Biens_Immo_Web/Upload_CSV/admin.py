from django.contrib import admin
from .models import Immo


# Register your models here.

@admin.register(Immo)
class RequestAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Immo._meta.get_fields()]
  search_fields = ['departement']
