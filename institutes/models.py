import binascii
import datetime

from django.db import models

from master.models import ImsBaseModel


class Institute(ImsBaseModel):
    identifier = models.CharField(max_length=100, null=True, blank=False, default=None)
    name = models.CharField(max_length=100, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField()
    phone = models.CharField(max_length=12, null=True, blank=False)
    mobile = models.CharField(max_length=12, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    objective = models.TextField()

    bord = models.CharField(max_length=155, null=True, blank=False)
    ownership = models.CharField(max_length=155, null=True, blank=False)
    documents = models.CharField(max_length=155, null=True, blank=False)

    tan = models.CharField(max_length=155, null=True, blank=False)
    license = models.CharField(max_length=155, null=True, blank=False)
    accreditation = models.CharField(max_length=155, null=True, blank=False)
    approvals = models.CharField(max_length=155, null=True, blank=False)
    declaration = models.CharField(max_length=155, null=True, blank=False)

    def __str__(self):
        return self.name

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        today = datetime.datetime.today()
        id_string = f"{today.day}{today.month}{today.year}{today.hour}{today.minute}{today.second}"
        self.identifier = binascii.hexlify(bytes(id_string, 'utf-8')).decode()
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)
