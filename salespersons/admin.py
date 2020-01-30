from django.contrib import admin
from salespersons.models import SalesPersonUser

class SalesPersonUserAdmin(admin.ModelAdmin):
    # ...
    list_display = ('first_name', 'last_name', 'username', 'role', 'manager')

admin.site.register(SalesPersonUser, SalesPersonUserAdmin)
