# Rest Framework
from rest_framework import serializers
from file.serializers import FileSerializer

# Project
from user.models.base import User, Position


class DayField(serializers.Field):

    def to_representation(self, value):
        if value == 0:
            return "Happy Birthday!!!"
        return "%d day left" % value


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', "image", 'first_name', 'last_name', 'position', 'phone_number', 'telegram', 'birthday', 'work_type')
        depth = 1


class UserListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'position', 'image', 'work_type')
    
    def to_representation(self, instance):
        self.fields['position'] = PositionSerializer(many=True)
        self.fields['image'] = FileSerializer(context=self.context)
        return super(UserListSerializer, self).to_representation(instance)


class BirthdayListSerializer(serializers.HyperlinkedModelSerializer):
    day = DayField()

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'image', 'work_type', 'birthday', 'day')
    
    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(context=self.context)
        return super(BirthdayListSerializer, self).to_representation(instance)
