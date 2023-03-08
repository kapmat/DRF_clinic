from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import RecordsSerializer
from .models import Records
from .permissions import IsOwner

class RecordsAPIList(generics.ListCreateAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer
    permission_classes = (IsAdminUser, )


class RecordsDitailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer
    permission_classes = (IsOwner, )











# class RecordsViewSet(viewsets.ModelViewSet):
#     queryset = Records.objects.all()
#     serializer_class = RecordsSerializer

