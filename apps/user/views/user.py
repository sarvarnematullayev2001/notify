# Rest Framework
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics

# Project
from user.serializers.user import UserSerializer, UserListSerializer, BirthdayListSerializer
from user.models import User

# Django
from django.db.models import F
from django.shortcuts import get_object_or_404

# Python
from datetime import datetime


class UserViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    search_fields = ['username', 'first_name', 'last_name', 'position__position']

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserSerializer


class BirthdayListAPIView(generics.ListAPIView):
    serializer_class = BirthdayListSerializer
    search_fields = ['username', 'first_name', 'last_name', 'position__position']

    def get_queryset(self):
        return User.objects.filter(birthday__month=datetime.now().month, 
                                   birthday__day__gte=datetime.now().day).order_by(
            'birthday__day').annotate(day=F('birthday__day') - datetime.now().day)


class ProfileRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)