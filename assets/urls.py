from django.urls import path
from .views import verify_asset

urlpatterns = [
    path("verify/", verify_asset),
]
