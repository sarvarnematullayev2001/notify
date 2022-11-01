# Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser

# Project
from notify.models.late import Lateness
from notify.serializers.late import LatenessSerializer


class LatenessViewSet(ModelViewSet):
    queryset = Lateness.objects.all()
    serializer_class = LatenessSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Lateness.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


__all__ = (
    'LatenessViewSet',
)