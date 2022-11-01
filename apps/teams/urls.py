# Django
from django.urls import path

# Project
from teams.views import ProjectListAPIView, ProjectDetailAPIView


urlpatterns = [
    path('', ProjectListAPIView.as_view()),
    path('<int:pk>/', ProjectDetailAPIView.as_view(), name='team-detail')
]