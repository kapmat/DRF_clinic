from rest_framework import viewsets
from serialozers import RecordsSerializer
from .models import Records


class RecordsViewSet(viewsets.ViewSet):
    queryset = Records.object.all()
    serializer_class = RecordsSerializer

