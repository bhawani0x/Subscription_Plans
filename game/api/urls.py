from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('customer/', UserCustomer.as_view(), name='users'),
    path('customer/<int:pk>/', UserCustomer_details.as_view(), name='user-profile-detail'),
    path('', include(router.urls)),
]
