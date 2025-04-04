"""
    serializer to access dashboards
"""

from rest_framework import serializers
from dashboard.models import Dashboards


class DashBoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dashboards
        fields = '__all__'