from django.urls import path
from .views import buffer, recalculation, stock_item_days,  stock_forecast_days, StockForecastDaysView, order_required,order_required_3



urlpatterns = [
    path('buffer/', buffer, name='buffer'),
    path('recalculation/', recalculation, name='recalculation'),
    path('stock_item_days/', stock_item_days, name='stock_item_days'),
    path('stock_forecast_days/', stock_forecast_days, name='stock_forecast_days'),
    path('stock_in_days/', StockForecastDaysView.as_view(), name='stock_in_days'),
    path('order_required', order_required, name='order_required'),
    path('order_required_3', order_required_3, name='order_required_3'),
    
    
]
   