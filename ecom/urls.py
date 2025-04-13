"""
defines url mapping for dashboard API
"""

from django.urls import path
from ecom.views.EcomRecommenderView import EcomRecommenderView
from ecom.views.EcomUserView import EcomUserView
from ecom.views.EcomCountryView import EcomCountryView

urlpatterns = [
    path("country/", EcomCountryView.as_view()),
    path("user/", EcomUserView.as_view()),
    path("recommend/", EcomRecommenderView.as_view()),
]
