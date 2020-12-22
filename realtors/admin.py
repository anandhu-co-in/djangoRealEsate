from django.contrib import admin

# Register your models here.
from .models import Realtor


# i havent created the list modificication class here, kep this as default

admin.site.register(Realtor)