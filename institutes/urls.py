from django.urls import path
from rest_framework import routers

from institutes.api_views import ListInstitutesApi
from institutes.views import CreateInstitute, ManageInstitute

app_name = 'institutes'
api_version = 'v1'
router = routers.SimpleRouter()

router.register(f'api/{api_version}/', ListInstitutesApi)


urlpatterns = [
    path('create/', CreateInstitute.as_view(), name='create'),
    path('manage/<ins_identifier>/', ManageInstitute.as_view(), name='manage'),

    # Django Rest API Urls
    # path(', ListInstitutesApi.as_view(), name='institute_list_api'),
]

urlpatterns += router.urls
