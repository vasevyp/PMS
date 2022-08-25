from django.urls import path
from .views import buffer, recalculation



urlpatterns = [
    path('buffer/', buffer, name='buffer'),
    path('recalculation/', recalculation, name='recalculation')
    
]
   