from salespersons.models import SalesPersonUser
from leads.models import Lead


def assign_salesperson():
    leadcount_per_salesperson = {}
    salespersonlist = SalesPersonUser.objects.filter(is_superuser= False)
    for salesperson in salespersonlist:
        salesperson_leads = Lead.objects.filter(assigned_to=salesperson.id)
        leadcount_per_salesperson[salesperson]=len(salesperson_leads)
    leadcount_per_salesperson_tuple = sorted(leadcount_per_salesperson.items(), key=lambda x: x[1])
    return leadcount_per_salesperson_tuple[0][0]


        
