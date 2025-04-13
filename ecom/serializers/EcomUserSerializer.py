"""
    serializer to access dashboards
"""

from rest_framework import serializers
from ecom.models import CustomerSummary, EcomCountry


class EcomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerSummary
        fields = '__all__'