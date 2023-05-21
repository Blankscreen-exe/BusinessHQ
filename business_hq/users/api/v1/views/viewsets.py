from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.decorators import login_required

from users.models import User
from users.api.v1.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """Viewset for handling api calls to ServiceModel
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO: no need for permissions for this one
    # permission_classes = [IsAdminUser, IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Custom logic for authenticated user
            pass

        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        if request.user.is_admin:
            # Custom logic for admin user
            pass

        return super().create(request, *args, **kwargs)
    
    @login_required
    def destroy(self, request, *args, **kwargs):
        if request.user.is_admin:
            # Custom logic for authenticated admin user
            pass

        return super().destroy(request, *args, **kwargs)

# TODO: view for customer creation
# TODO: view for customer self retrieval
# TODO: view for customer self update
# TODO: view for customer self delete


# TODO: view for manager CRUD
# TODO: view for customer handler CRUD


    
    
    