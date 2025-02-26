from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'flocks', FlockView) 


urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
