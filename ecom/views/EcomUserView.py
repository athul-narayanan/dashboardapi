from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from ecom.models import CustomerSummary
from ecom.serializers.EcomUserSerializer import EcomUserSerializer

class EcomUserView(generics.GenericAPIView):
    """
    Accepts:
    {
        "country": "Norway",
        "page": 2
    }
    """
    serializer_class = EcomUserSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        country = request.data.get("country")
        page = request.data.get("page", 1)

        # Filter and sort
        queryset = CustomerSummary.objects.all()
        if country:
            queryset = queryset.filter(country__iexact=country)

        queryset = queryset.order_by('-invoice_count')

        # Inject page into request manually
        request.query_params._mutable = True
        request.query_params["page"] = str(page)

        # Paginate and serialize
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_queryset(queryset, request, view=self)
        serializer = self.get_serializer(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)
