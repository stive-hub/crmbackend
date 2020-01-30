from django.shortcuts import render
from django.contrib.auth import logout
from salespersons.models import SalesPersonUser
from django.db.models import Q
from leads.models import Lead

# Create your views here.
def index(request):
    queryset = []
    context = {}
    try:
        if request.user.is_superuser:
            queryset = Lead.objects.all()
        else:
            user = SalesPersonUser.objects.filter(email=request.user).first()
            queryset = Lead.objects.filter(assigned_to=user.id)
    except:
        pass
    
    context['Leads'] = queryset
    return render(request, 'ui/index.html', context)

def uilogout(request):
    logout(request)
    return render(request, 'ui/index.html')

def test(request):
    return render(request,"ui/index_vivek.html")
