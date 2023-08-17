from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save


class ImsBaseModel(models.Model):
    created_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='created_by')
    updated_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='updated_by')
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True, auto_created=True)
