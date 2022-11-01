from rest_framework import serializers
from user.models.base import User

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = []

    def to_representation(self, instance):
        representation = super(StatSerializer, self).to_representation(instance)
        representation['remote_stats'] = instance.remote_set.count()
        representation['late_stats'] = instance.lateness.count()
        representation['timeoff_stats'] = instance.timeoff_set.count()
        representation['warn_stats'] = instance.warn_set.count()
        return representation
