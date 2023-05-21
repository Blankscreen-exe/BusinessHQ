from django.urls import path
from .views.viewsets import get_route

urlpatterns = [
    path("", get_route, name="test"),
]
