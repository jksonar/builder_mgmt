from django.db import models
from users.models import User

class BuilderCompany(models.Model):
    name = models.CharField(max_length=200)
    license_number = models.CharField(max_length=50)
    registration_date = models.DateField()
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)

class Builder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)