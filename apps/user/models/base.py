# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password

# Project
from file.models import File
from core.base_model import BaseModel


class Position(BaseModel):

    POSITION = (
        ('HR', 'HR'),
        ('Project Manager', 'Project Manager'),
        ('Web Designer', 'Web Designer'),
        ('Frontend Engineer', 'Frontend Engineer'),
        ('Backend Engineer', 'Backend Engineer'),
        ('Mobile Engineer', 'Mobile Engineer'),
        ('Marketer', 'Marketer'),
        ('Manager', 'Manager')
    )
    position = models.CharField(max_length=70, choices=POSITION, unique=True)

    def __str__(self):
        return self.position


class User(AbstractUser):
    ABSENT = 'Absent'
    AT_OFFICE = 'At office'
    REMOTE = 'Remote'
    WORK_TYPE = (
        (ABSENT, ABSENT),
        (AT_OFFICE, AT_OFFICE),
        (REMOTE, REMOTE)
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+998(12)345 67 89'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, blank=True)
    position = models.ManyToManyField(Position, null=True)
    work_type = models.CharField(max_length=30, choices=WORK_TYPE, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    telegram = models.CharField(max_length=70, validators=[MinLengthValidator(4)])
    image = models.OneToOneField(File, on_delete=models.CASCADE, related_name='image', null=True, blank=True)
    
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.pk and self.password and not self.is_staff:
            self.password = make_password(self.password)
        return super(User, self).save(*args, **kwargs)


class HardwareAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hardware')
    mac_address = models.CharField(max_length=19)

    def __str__(self):
        return f"{self.user.username} | {self.mac_address}"

    class Meta:
        verbose_name_plural = "Hardware Addresses"