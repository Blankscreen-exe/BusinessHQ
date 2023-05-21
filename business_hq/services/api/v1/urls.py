from django.urls import path
from .viewsets import ServicesListView, ServiceView

urlpatterns = [
    path('services/list/', ServicesListView.as_view(), name='services-list'),
    path('services/<int:pk>/', ServiceView.as_view(), name='service-single'),
]