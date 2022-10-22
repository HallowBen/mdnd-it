from django.contrib import admin
from .models import Rating, Contact
# Register your models here.

class ratingadmin(admin.ModelAdmin):
    readonly_fields=('date',)

admin.site.register(Rating, ratingadmin)

admin.site.register(Contact, ratingadmin)
