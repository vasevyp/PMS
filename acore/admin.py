from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from  .models import Sales, SellForecast, DailyRequirement 
# Register your models here.
@admin.register(Sales)
class SalesAdmin(ImportExportModelAdmin):
    list_display = [ 'name', 'quantity','date' ]
    save_on_top = True
    search_fields = ['name', 'date']
    list_filter= ('name', 'date')
    
@admin.register(SellForecast)
class SellForecastAdmin(ImportExportModelAdmin):
    list_display = [ 'name', 'category', 'weekday_forecast', 'weekend_forecast', 'avrg_forecast', 'holiday_forecast', 'promotion_forecast' ]
    save_on_top = True
    search_fields = ['name', 'category']
    list_filter= ('name', 'category')   
    
@admin.register(DailyRequirement)
class DailyRequirementAdmin(ImportExportModelAdmin):
    list_display = [ 'product', 'code', 'avrg_forecast','ingredient', 'code_ingr', 'ratio', 'daily_requirement' ]
    save_on_top = True
    search_fields = ['product', 'code_ingr', 'ingredient']
    list_filter= ('product', 'ingredient')     
    
    