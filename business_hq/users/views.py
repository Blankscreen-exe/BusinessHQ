from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from users.models import User
from users.serializers import UserSerializer

class RegisterView(APIView):
    """Registers users
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)


class LoginView(APIView):
    """Login for customers
    """
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        
        if user is None:
            # TODO: change error message
            raise AuthenticationFailed('User Not Found dumbass')
        
        if not user.check_password(password):
            # TODO: change error message
            raise AuthenticationFailed('Password not correct BHAAAGA')
        
        return Response(user)
             
        