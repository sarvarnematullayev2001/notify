# Rest Framework
from rest_framework.routers import DefaultRouter

# Django
from django.urls import path

# Project
from .views.login import LoginAPIView
from .views.user import UserViewSet, BirthdayListAPIView, ProfileRetrieveAPIView
from .views.mac import MacAPIView

router = DefaultRouter()
router.register('', UserViewSet, basename='user')

urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('birthday/', BirthdayListAPIView.as_view()),
    path('devices/', MacAPIView.as_view()),
    path('profile/', ProfileRetrieveAPIView.as_view()),
]

urlpatterns += router.urls