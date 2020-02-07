from django.shortcuts import render
from rest_framework import viewsets
from leads.models import Lead

from salespersons.models import SalesPersonUser
from leads.serializers import LeadSerializer, LeadGetSerializer
from django.http import HttpResponse

from mailengine.models import EventLog
from mailengine.tasks import followup

from django.core.mail import send_mail

# Create your views here.


class LeadModelView(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return LeadGetSerializer
        else:
            return self.serializer_class
    
    # def partial_update(self, request, pk=None):
    #     if request.PATCH['status']:
    #         pass
    #     elif request.PATCH['assigned_to']:
    #         pass
    #     return

    #permission_classes = (IsAdminUser,)

    # def retrieve(self, request, pk):
    #     context={
    #         'is_lead_updated': False,
    #         'lead' : pk
    #     }
    #     return render(request, 'ui/lead.html', context=context)


# def reassign(request, pk):
#     if request.method == 'POST':
#         new_salesperson = request.POST['new_salesperson']
#         salesperson_assigned = SalesPersonUser.objects.filter(first_name=new_salesperson).first()
#         lead_obj = Lead.object.get(pk)
#         lead_obj.assigned_to = salesperson_assigned.id
#         lead_obj.save()
#         eventlog_obj = EventLog(event_lead=lead_obj, event_type="New Lead",
#                                 salesperson=lead_obj.assigned_to, manager=lead_obj.assigned_to.first().manager.first())
#         eventlog_obj.save()
#         send_mail('Testing',
#                   'Lead Assigned',
#                   'tempbytedeveloper@gmail.com',
#                   ['jithinjkumar@gmail.com'],
#                   fail_silently=False,)
#         followup.delay(eventlog_obj)
#         context = {
#             'is_lead_updated': True,
#             'message': f"Lead Reassigned to { Lead.assigned_to } !",
#             'lead': lead_obj
#         }
#         return render(request, 'ui/lead.html', context=context)
#     elif request.method == 'GET': 
#         context = {
#             'is_lead_updated': False,
#             'message':None,
#             'lead': Lead.objects.get(pk)
#         }
#         return render(request, 'ui/lead.html', context=context)


# def update_lead_status(self, request, pk):
#     new_status = request.POST['new_status']
#     lead_obj = Lead.object.get(pk)
#     lead_obj.status = new_status
#     lead_obj.save()
#     eventlog_obj = EventLog(event_lead=lead_obj, event_type="New Lead",salesperson=lead_obj.assigned_to, manager=lead_obj.assigned_to.first().manager.first())
#     eventlog_obj.save()
#     followup.delay(eventlog_obj)
#     context = {
#         'is_lead_updated': True,
#         'message': f"Lead updated to { Lead.status } !",
#         'lead': lead_obj
#     }
#     return render(request, 'ui/lead.html', context) 
