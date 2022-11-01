from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from user.models.base import User
from stats.serializers.stats import StatSerializer


class StatisticsList(ListAPIView):
    serializer_class = StatSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)