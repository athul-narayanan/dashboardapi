"""
defines url mapping for dashboard API
"""

from django.urls import path
from dashboard.views.DashBoardView import DashBoardView
from dashboard.views.QuestionView import QuestionGeminiView


urlpatterns = [
    path('', DashBoardView.as_view()),
    path('/ask', QuestionGeminiView.as_view())
]