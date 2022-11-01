from datetime import date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum, F
from user.models import User
from notify.models.late import Lateness


class LateHoursView(APIView):
    queryset = User.objects.all()

    def get(self, request):
        late = Lateness.objects.filter(user=request.user, created_datetime__year=date.today().year).values(
            month=F("created_datetime__month")).annotate(hours=Sum('total')).filter(hours__gt=0).order_by(
            "created_datetime__month")
        statistics = {"Late Hours": late}
        return Response(statistics, status=status.HTTP_200_OK)

