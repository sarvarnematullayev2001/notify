import datetime
from django.db import models
from core.base_model import BaseModel
from user.models.base import User


class Remote(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    reason = models.TextField()

    def __str__(self) -> str:
        return f"{self.user} for {self.days_off()}"

    def days_off(self):
        return str(self.date - datetime.date.today()).split(',')[0]