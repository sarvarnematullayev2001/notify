from rest_framework import serializers
from user.models.base import User
from django.db.models import Sum


class LateHoursSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = []

    def to_representation(self, instance):
        representation = super(LateHoursSerializer, self).to_representation(instance)
        hour = instance.lateness_set.aggregate(Sum('hour'))
        minutes = instance.lateness_set.aggregate(Sum('minutes'))
        representation['late_hours'] = hour['hour__sum'] + (minutes['minutes__sum']//60)
        return representation