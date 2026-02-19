from django.urls import path
from . import views

urlpatterns = [
    path('create-submission/', views.create_submission),
]
