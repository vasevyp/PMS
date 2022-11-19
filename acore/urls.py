from django.urls import path, re_path
# from wkhtmltopdf.views import PDFTemplateView, TemplateView, PDFTemplateResponse
# from django_pdfkit import PDFView

from .views import  recalculation, stock_item_days,  stock_forecast_days, StockForecastDaysView, order_required,order_required_3, order, order_print,  pdfprint, order_item_edit_form, order_delete,order_calc, last_order, OrderListView



urlpatterns = [    
    path('recalculation/', recalculation, name='recalculation'),
    path('stock-item-days/', stock_item_days, name='stock_item_days'),
    path('stock-forecast-days/', stock_forecast_days, name='stock_forecast_days'),
    path('stock-in_days/', StockForecastDaysView.as_view(), name='stock_in_days'),
    path('order-required', order_required, name='order_required'),
    path('order-required_3', order_required_3, name='order_required_3'),
    path('order-calc',order_calc, name='order_calc'),
    path('order', order, name='order'),
    path('order-edit/<int:id>', order_item_edit_form, name='order_edit_form'),
    path('order-delete/<int:id>', order_delete, name='order_delete'),
    path('order-print', order_print, name='order_print'),
    path('print', pdfprint, name='my-pdf'),    
    path('orders-list/', OrderListView.as_view(), name='orders_list'),
    path('last-order', last_order, name='last_order'),
    
    
    
    
]
