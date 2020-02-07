from rest_framework import serializers
from salespersons.models import SalesPersonUser

class SalesPersonUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SalesPersonUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'manager', 'is_superuser']
