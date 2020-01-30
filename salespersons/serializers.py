from rest_framework import serializers
from salespersons.models import SalesPersonUser


class SalesPersonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPersonUser
        fields = "__all__"
