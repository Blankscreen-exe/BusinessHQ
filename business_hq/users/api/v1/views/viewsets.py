from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.authentication import JWTAuthentication


from users.models import User
from users.api.v1.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """Viewset for handling api calls to ServiceModel
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO: no need for permissions for this one
    # permission_classes = [IsAdminUser, IsAuthenticated]
    
    # TODO: permissions = Manager, Admin
    def list(self, request, *args, **kwargs):
        # allow this method only if the user is admin
        
        jwt_authentication = JWTAuthentication()
        user = request.user.username
        print("=======================", user)
        
        if request.user.is_authenticated and request.user.is_superuser:
            # TODO: TODO: Custom logic for authenticated user
            print(f"MESSAGE: The user {user} is authorized to see all users")
        print(f"MESSAGE: The user {user} is NOT authorized to see all users")
         

        return super().list(request, *args, **kwargs)
    
    # TODO: permissions = Customer, Admin
    def create(self, request, *args, **kwargs):
        try:
            if request.user.is_superuser:
                # TODO: Custom logic for admin user
            print(" THIS USER IS SUPER USER")
                print("==========", request.user.get_profile().username)
                pass
        except:
            pass
        print(" THIS USER IS NOT SUPER USER")

        return super().create(request, *args, **kwargs)
    
    # TODO: permissions = Admin, Customers
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
# TODO: view for customer handler CR


    
    
    