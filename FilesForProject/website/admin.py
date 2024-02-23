from django.contrib import admin
from . models import Drug, Patient, Route, Transaction
# Register your models here.
admin.site.register(Drug)
admin.site.register(Route)
admin.site.register(Transaction)

admin.site.site_header  =  "Outpatient Medication System: Pre-op Anaemia Clinic - Admin Portal"  
admin.site.index_title  =  "Outpatient Medication System: Pre-op Anaemia Clinic"
admin.site.site_title  =  "Admin portal"