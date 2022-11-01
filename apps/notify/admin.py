# Django
from django.contrib import admin

# Project
from notify.models.late import Lateness
from notify.models.remote import Remote
from notify.models.timeoff import Timeoff

admin.site.register(Remote)
admin.site.register(Timeoff)


@admin.register(Lateness)
class LatenessAdmin(admin.ModelAdmin):
    list_display = ('user', 'hour', 'minutes', 'created_datetime')
    exclude = ('total',)
