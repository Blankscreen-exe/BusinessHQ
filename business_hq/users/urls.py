from django.urls import path


from users.views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='customer-register'),
    path('login/', LoginView.as_view(), name='customer-login'),
]