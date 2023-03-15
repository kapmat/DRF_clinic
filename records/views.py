from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RecordsSerializer
from .models import Records
from .permissions import IsUserDitail


class AllRecordsAPIList(generics.ListAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer


class RecordsUserAPIList(generics.ListCreateAPIView):
    serializer_class = RecordsSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return Records.objects.filter(user=user)


class RecordsDitailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer
    permission_classes = (IsUserDitail, )
