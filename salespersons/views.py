from django.shortcuts import render
from rest_framework import viewsets
from salespersons.models import SalesPersonUser
from salespersons.serializers import SalesPersonUserSerializer


class SalesPersonUserModelView(viewsets.ModelViewSet):
    queryset = SalesPersonUser.objects.all()
    serializer_class = SalesPersonUserSerializer
    #permission_classes = (IsAdminUser,)
