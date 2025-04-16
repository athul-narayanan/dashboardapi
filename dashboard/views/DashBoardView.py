from rest_framework import generics
from rest_framework.response import Response
from dashboard.models import Dashboards
from dashboard.serializers.DashBoardSerializer import DashBoardSerializer




class DashBoardView(generics.GenericAPIView):
    """
        This file is used manage dashboard data
    """

    def get(self, request):
        """
            Fetch all dashboards
        """
        dashboards =  Dashboards.objects.filter()
        serializedData = DashBoardSerializer(dashboards, many=True)
        dashboard_data = {}
        for item in serializedData.data:
            key = item['title']
            if key not in dashboard_data:
                dashboard_data[key] = {
                    'type': item['type'],
                    'dashboards': []
                }
            
            dashboard_data[key]['dashboards'].append({
                'name': item['name'],
                'link': item['link'],
                "title": key
            })
        final_dashboards = [
                {
                    'type': data['type'], 
                    'title': key,
                    'dashboards': data['dashboards']
                } for key, data in dashboard_data.items()
            ]
        return Response(final_dashboards)