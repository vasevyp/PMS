from django import forms
from django.forms import ModelForm
from .models import BuyItem, SaleProduct

class BuyItemForm(ModelForm):
    class Meta:
        model = BuyItem
        fields=['name', 'code', 'unit', 'unit_cost', 'quantity' ]
        widgets={
            'name':forms.Select(attrs={'class':'form-control'}),
            'code':forms.Select(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'},),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),              
        }
        
class SoldProductForm(ModelForm):
    class Meta:
        model=SaleProduct 
        fields=['name','sold','unit' ]
        widgets={
            'name':forms.Select(attrs={'class':'form-control'}),
            'sold':forms.NumberInput(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'},),              
        }                  