import binascii
import datetime

from django.contrib.auth import get_user_model
from django.db import models

from institutes.models import Institute


class Employee(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100, null=True, blank=False, default=None)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        today = datetime.datetime.today()
        id_string = f"{today.day}{today.month}{today.year}{today.hour}{today.minute}{today.second}"
        self.identifier = binascii.hexlify(bytes(id_string, 'utf-8')).decode()
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)
