from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from users.models import User
from users.serializers import UserSerializer

