# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Python
import json

class MacAPIView(APIView):

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        mac_list = json.loads(body_unicode)
        user = request.user
        print(mac_list)
        queryset = user.hardware.filter(mac_address__in=mac_list)
        if user.work_type != 'Remote':
            user.work_type = 'At office' if queryset.exists() else 'Absent'
            user.save()
        return Response({'response': 'Request sent'}, status=200)