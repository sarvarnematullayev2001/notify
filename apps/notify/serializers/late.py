# Rest Framework
from dataclasses import fields
from rest_framework import serializers
from apps.user.serializers.user import UserSerializer

# Models
from notify.models.late import Lateness


class LatenessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lateness
        fields = ['pk', 'hour', 'minutes']


__all__ = (
    'LatenessSerializer',
)