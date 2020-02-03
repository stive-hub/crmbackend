from rest_framework import serializers
from leads.models import Lead, LeadStage
from salespersons.models import SalesPersonUser
from mailengine.models import EventLog
from leads.utils import assign_salesperson
from django.utils import timezone
from django.core.mail import send_mail


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        # exclude = ['assigned_to']
        read_only_fields = ['assigned_to', 'status']
        depth = 1
    
    def create(self, validated_data):
        lead_object = Lead(status=LeadStage.objects.filter(id=1).first(),**validated_data)
        lead_object.save()
        lead_object.assigned_to.set([assign_salesperson()])
        lead_object.save()
        try:
            eventlog_obj = EventLog(event_lead=lead_object, event_type="New Lead",
                                    salesperson=lead_object.assigned_to, manager=manager)
        except:
            eventlog_obj = EventLog(event_lead=lead_object, event_type="New Lead",
                                    salesperson=SalesPersonUser.objects.get(pk=1), manager=SalesPersonUser.objects.get(pk=1))  
        print("about to send mail")      
        send_mail('Testing',
                  'New Lead',
                  'tempbytedeveloper@gmail.com',
                  ['jithinjkumar@gmail.com'],
                  fail_silently=False,)
        return lead_object





    
