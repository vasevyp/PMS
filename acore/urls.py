from django.urls import path
from .views import buffer



urlpatterns = [
    path('buffer/', buffer, name='buffer'),
]
   