from rest_framework import serializers

from institutes.models import Institute


class InstituteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = '__all__'
