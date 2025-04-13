from rest_framework import generics
from rest_framework.response import Response
from ecom.models import EcomCountry
from ecom.serializers.EcomCountrySerializer import EcomCountrySerializer

class EcomCountryView(generics.GenericAPIView):
    """
    This view is used to fetch all countries
    """
    serializer_class = EcomCountrySerializer
    
    def get(self, request):
        ecomCountry = EcomCountry.objects.all()
        serializedData = EcomCountrySerializer(ecomCountry, many=True)
        return Response(serializedData.data)