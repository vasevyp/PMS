from django.urls import path, re_path
# from wkhtmltopdf.views import PDFTemplateView, TemplateView, PDFTemplateResponse
# from django_pdfkit import PDFView

from .views import  recalculation, stock_item_days,  stock_forecast_days, StockForecastDaysView, order_required,order_required_3, order, order_print,  pdfprint, order_item_edit_form, order_delete,order_calc



urlpatterns = [    
    path('recalculation/', recalculation, name='recalculation'),
    path('stock_item_days/', stock_item_days, name='stock_item_days'),
    path('stock_forecast_days/', stock_forecast_days, name='stock_forecast_days'),
    path('stock_in_days/', StockForecastDaysView.as_view(), name='stock_in_days'),
    path('order_required', order_required, name='order_required'),
    path('order_required_3', order_required_3, name='order_required_3'),
    path('order', order, name='order'),
    path('order_edit/<int:id>', order_item_edit_form, name='order_edit_form'),
    path('order_delete/<int:id>', order_delete, name='order_delete'),
    path('order-print', order_print, name='print'),
    path('print', pdfprint, name='my-pdf'),
    path('order-calc',order_calc, name='order_calc')
    
    
    
]
