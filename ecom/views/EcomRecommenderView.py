from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from ecom.ml.productrecommender import ProductRecommender
import pandas as pd
import os

class EcomRecommenderView(generics.GenericAPIView):
    def get(self, request):
        country = request.query_params.get('country')
        user_id = request.query_params.get('user_id')

        if not country or not user_id:
            return Response({'error': 'Both country and user_id are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user_id = int(user_id)
        except ValueError:
            return Response({'error': 'user_id must be an integer.'}, status=status.HTTP_400_BAD_REQUEST)

        # Load dataset
        csv_path = os.path.join('ecom\data\data.csv')
        df = pd.read_csv(csv_path)
        recommender = ProductRecommender(df)

        try:
            recommended = recommender.recommend_products(country, user_id)
            return Response({
                'user_id': user_id,
                'country': country,
                'recommended_products': recommended
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
