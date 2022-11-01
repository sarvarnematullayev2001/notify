from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from notify.models.warn import Warn
from notify.serializers.warn import WarnSerializer


class WarnViewSet(ModelViewSet):
    queryset = Warn.objects.all()
    serializer_class = WarnSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)