from rest_framework import viewsets
from .serializers import RecordsSerializer
from .models import Records


class RecordsViewSet(viewsets.ModelViewSet):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer

