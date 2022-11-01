# Django
from django.contrib import admin

# Project
from .models import User, Position, HardwareAddress


class MacInline(admin.StackedInline):
    model = HardwareAddress
    extra = 3


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'telegram')
    inlines = [MacInline]

admin.site.register(Position)