from django.contrib import admin
from django.urls import path, include
from services.views import *
from records.views import *
# from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'services', ServicesPublicViewSet)
# router.register(r'records', RecordsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/authorization/', include('rest_framework.urls')),
    path('api/v1/services/', ServicesPublicAPIList.as_view()),
    path('api/v1/services-list/', AllServicesViewSet.as_view()),
    path('api/v1/services-list/<int:pk>', ServicesDitailAPIView.as_view()),
    path('api/v1/records/', RecordsUserAPIList.as_view()),
    path('api/v1/records/<int:pk>', RecordsDitailAPIView.as_view()),
    path('api/v1/records-list/', AllRecordsAPIList.as_view()),
    # path('api/v1/', include(router.urls)),
]
