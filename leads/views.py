from django.shortcuts import render
from rest_framework import viewsets
from leads.models import Lead
from leads.serializers import LeadSerializer
from django.http import HttpResponse
# Create your views here.


class LeadModelView(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    #permission_classes = (IsAdminUser,)
