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
        fields=['name', 'code','category', 'supplier', 'unit','unit_cost', 'description', 'delivery_time', 'supply_lot', 'lot_weight', 'lot_length', 'lot_width', 'lot_height', 'best_befor']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id': 'product'}),
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'supplier':forms.Select(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'},),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control',  'rows':3}),
            'delivery_time':forms.NumberInput(attrs={'class':'form-control'}), 
            'supply_lot':forms.NumberInput(attrs={'class':'form-control'}), 
            'lot_weight':forms.NumberInput(attrs={'class':'form-control'}), 
            'lot_length':forms.NumberInput(attrs={'class':'form-control'}), 
            'lot_width':forms.NumberInput(attrs={'class':'form-control'}), 
            'lot_height':forms.NumberInput(attrs={'class':'form-control'}), 
            'best_befor':forms.TextInput(attrs={'class':'form-control'})
              
        }           
        
class AddProductForm(ModelForm):
    # price= forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields=['name', 'code','category', 'difficulty', 'price', 'description', 'cooking']
        # field_classes={'price':DecimalField}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','id': 'product'}),
            'code':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'difficulty':forms.Select(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'},),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'cooking':forms.TextInput(attrs={'class':'form-control'}),
              
        }                          
        
class AddRecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields=['product','code','ingredient', 'code_ingr','unit', 'unit_cost', 'ratio']
        field_classes={'unit_cost':DecimalField, 'quantity':DecimalField}
        widgets={
            'product':forms.Select(attrs={'class':'form-control','id': 'product'}),
            'code':forms.NumberInput(attrs={'class':'form-control'}),
            'ingredient':forms.Select(attrs={'class':'form-control'}),
            'code_ingr':forms.NumberInput(attrs={'class':'form-control'}),
            'unit':forms.Select(attrs={'class':'form-control'}),
            'unit_cost':forms.NumberInput(attrs={'class':'form-control'}),
            'ratio':forms.NumberInput(attrs={'class':'form-control'}),
        }             
        
# class AddImpexProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields=['ingredient']        

