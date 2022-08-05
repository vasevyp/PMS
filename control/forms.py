from django import forms
from django.forms import ModelForm
from .models import BuyItem, SaleProduct

class BuyItemForm(ModelForm):
    class Meta:
        model = BuyItem
        fields=['name',  'unit', 'unit_cost', 'quantity','supplier', 'invoice' ]
        widgets={
            'name':forms.Select(attrs={'class':'form-control'}),        
            'unit':forms.Select(attrs={'class':'form-control'},),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
            'supplier':forms.Select(attrs={'class':'form-control'},),
            'invoice':forms.TextInput(attrs={'class':'form-control'})              
        }
        
class SoldProductForm(ModelForm):
    class Meta:
        model=SaleProduct 
        fields=['name','unit','sold', ]
        widgets={
            'name':forms.Select(attrs={'class':'form-control'}),            
            'unit':forms.Select(attrs={'class':'form-control'},),
            'sold':forms.NumberInput(attrs={'class':'form-control'}),
                         
        }                  