from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Donor)
admin.site.register(DonationDrive)
admin.site.register(RFIDTag)