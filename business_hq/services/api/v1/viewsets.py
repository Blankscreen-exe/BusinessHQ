from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from services.models import ServicesModel
from .serializers import ServicesSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    """Viewset for handling api calls to ServiceModel
    """
    queryset = ServicesModel.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]
    
class ServicesListView(APIView):
    """Secure separate view which Responds with a list of all available services.
    """
    def get(self, request):
        services = ServicesModel.objects.all()
        data = {'services': list(services.values())}
        return Response(data)

class ServiceView(APIView):
    """Shows details of a single service.
    """
    def get(self, request, pk):
        services = ServicesModel.objects.filter(pk=pk)
        # TODO: do a check to see if any results show up
        data = {'services': list(services.values())}
        return Response(data) 