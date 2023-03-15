from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Services
from .serializers import ServicesSerializer


class AllServicesViewSet(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDitailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesPublicAPIList(generics.ListAPIView):
    serializer_class = ServicesSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return Services.objects.filter(status=True)















# class ServicesAPIList(generics.ListCreateAPIView):
#    queryset = services.objects.all()
#    serializer_class = ServicesSerializer
#
#
# class ServicesAPIUpdate(generics.UpdateAPIView):
#    queryset = services.objects.all()
#    serializer_class = ServicesSerializer
#
#
# class ServicesAPIDitailView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = services.objects.all()
#    serializer_class = ServicesSerializer

# class ServicesAPIView(APIView):
#     def get(self, request):
#         w = services.objects.all()
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
#             instance = services.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = ServicesSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})


