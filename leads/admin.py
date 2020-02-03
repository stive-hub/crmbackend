from django.contrib import admin
from leads.models import Lead, LeadStage

# Register your models here.
admin.site.register(Lead)
admin.site.register(LeadStage)
