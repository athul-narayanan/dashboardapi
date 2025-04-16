"""
    serializer to access dashboards
"""

from rest_framework import serializers
from ecom.models import EcomCountry


class EcomCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EcomCountry
        fields = '__all__'