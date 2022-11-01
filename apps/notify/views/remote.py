from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from notify.models.remote import Remote
from notify.serializers.remote import RemoteSerializer


class RemoteViewSet(ModelViewSet):
    serializer_class = RemoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Remote.objects.all()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)