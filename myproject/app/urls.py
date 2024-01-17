from django.urls import path
from .views import ApiEndpoint, secret_page

urlpatterns = [
    path('hello/', ApiEndpoint.as_view(), name='hello'),
    path('secret/', secret_page, name='secret'),
]
