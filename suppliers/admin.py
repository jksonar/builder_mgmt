from django.contrib import admin

# Register your models here.
from .models import Supplier

admin.site.regiter(Supplier)