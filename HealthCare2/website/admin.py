from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Staff, Patient, Provider, Claim, ReasonForDenial,ServiceReceived

admin.site.register(Staff)
admin.site.register(Provider)
admin.site.register(Patient)
admin.site.register(Claim)
admin.site.register(ReasonForDenial)
admin.site.register(ServiceReceived)
