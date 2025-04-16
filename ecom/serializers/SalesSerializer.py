"""
    serializer to access dashboards
"""

from rest_framework import serializers
from ecom.models import Sales


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'