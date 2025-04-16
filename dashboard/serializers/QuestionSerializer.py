"""
    serializer to access dashboards
"""

from rest_framework import serializers
from dashboard.models import Dashboards


class DashBoardSerializer(serializers.Serializer):

    class Meta:
        fields = ["question", "filetype"]