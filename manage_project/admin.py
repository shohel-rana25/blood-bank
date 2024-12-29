from django.contrib import admin
from .models import Bloodlist

# Register your models here.

@admin.register(Bloodlist)
class BloodlistAdmin(admin.ModelAdmin):
    list_display=[fields.name  for fields in Bloodlist._meta.get_fields()]

