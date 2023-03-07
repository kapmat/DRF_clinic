from rest_framework import viewsets
from .models import *
from .serializers import *


class ServicesViewSet(viewsets.ModelViewSet):
   queryset = Services.objects.all()
   serializer_class = ServicesSerializer


class RecordViewSet(viewsets.ModelViewSet):
   queryset = Record.objects.all()
   serializer_class = RecordSerializer





# class ServicesAPIList(generics.ListCreateAPIView):
#    queryset = Services.objects.all()
#    serializer_class = ServicesSerializer
#
#
# class ServicesAPIUpdate(generics.UpdateAPIView):
#    queryset = Services.objects.all()
#    serializer_class = ServicesSerializer
#
#
# class ServicesAPIDitailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Services.objects.all()
#    serializer_class = ServicesSerializer

# class ServicesAPIView(APIView):
#     def get(self, request):
#         w = Services.objects.all()
#         return Response({'services': ServicesSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = ServicesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Services.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = ServicesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})








