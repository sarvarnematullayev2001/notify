# Django
from django.db import models

# Project
from core.base_model import BaseModel
from user.models import User


class Lateness(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lateness")
    hour = models.PositiveIntegerField()
    minutes = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.hour + self.minutes / 60
        super(Lateness, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.hour}:{self.minutes}"
