from django.contrib import admin

# Register your models here.
from .models import Builder, BuilderCompany

admin.site.register(Builder)
admin.site.register(BuilderCompany)