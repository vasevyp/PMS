from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field
 
from .models import  ImpexSaleProduct
 
class SaleProduct(forms.ModelForm):
    class Meta:
        model = ImpexSaleProduct
        fields=[ 'name','code','unit','price','sold','date' ,'created_date'
        ] 
        