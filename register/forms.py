from django import forms
from django.forms import ModelForm, DecimalField
from .models import Supplier, Category, CategoryItem, Item, Product, RecipeIngredient

class AddSupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields=['code', 'name','address', 'contact']
        widgets={
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'rows':3}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),            
        }



class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields=['code', 'name']
        widgets={
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'})
                    
        }
  
        

class AddCategoryItemForm(ModelForm):
    class Meta:
        model = CategoryItem
        fields=['code', 'name']
        widgets={
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'})
                    
        }
          
        
class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields=['name', 'code','category', 'supplier', 'unit','unit_cost', 'description', 'delivery_time', 'supply_pack', 'pack_weight', 'pack_length', 'pack_width', 'pack_height', 'best_befor']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id': 'product'}),
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'supplier':forms.Select(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'},),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control',  'rows':3}),
            'delivery_time':forms.NumberInput(attrs={'class':'form-control'}), 
            'supply_pack':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_weight':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_length':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_width':forms.NumberInput(attrs={'class':'form-control'}), 
            'pack_height':forms.NumberInput(attrs={'class':'form-control'}), 
            'best_befor':forms.DateInput(attrs={'type': 'date'})
              
        }           
        
class AddProductForm(ModelForm):
    # price= forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields=['name', 'code','category', 'difficulty', 'price', 'description', 'cooking', 'weekday_forecast', 'weekend_forecast', 'holiday_forecast', 'promotion_forecast']
        # field_classes={'price':DecimalField}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id': 'product'}),
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'difficulty':forms.Select(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'},),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'cooking':forms.TextInput(attrs={'class':'form-control'}),
            'weekday_forecast':forms.NumberInput(attrs={'class':'form-control'},),
            'weekend_forecast':forms.NumberInput(attrs={'class':'form-control'},),
            'holiday_forecast':forms.NumberInput(attrs={'class':'form-control'},),
            'promotion_forecast':forms.NumberInput(attrs={'class':'form-control'},),
              
        }                          
        
class AddRecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields=['product','ingredient', 'ratio']
        field_classes={'unit_cost':DecimalField, 'quantity':DecimalField}
        widgets={
            'product':forms.Select(attrs={'class':'form-control','id': 'product'}),
            'ingredient':forms.Select(attrs={'class':'form-control'}),
            # 'unit':forms.Select(attrs={'class':'form-control'}),
            'ratio':forms.NumberInput(attrs={'class':'form-control'}),
        }             
        
# class AddImpexProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields=['ingredient']        

