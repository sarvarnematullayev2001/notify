from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from notify.models.timeoff import Timeoff
from notify.serializers.timeoff import TimeoffSerializer


class TimeoffViewSet(ModelViewSet):
    serializer_class = TimeoffSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Timeoff.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)