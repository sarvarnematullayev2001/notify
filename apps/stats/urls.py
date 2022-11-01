from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.stats.views.history import HistoryList
from stats.views.feedback import FeedbackViewset
from stats.views.stats import StatisticsList
from stats.views.late_hours import LateHoursView


router = DefaultRouter()
router.register('feedback', FeedbackViewset, basename='feedback')

urlpatterns = [
    path('stats/', StatisticsList.as_view()),
    path('late_hours/', LateHoursView.as_view()),
    # path('work_hours/', WorkHoursView.as_view())
    path('history/', HistoryList.as_view()),
]

urlpatterns += router.urls
