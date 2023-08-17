from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from institutes.models import Institute
from institutes.serializers import InstituteSerializers


class ListInstitutesApi(ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializers
    permission_classes = [IsAuthenticated]
