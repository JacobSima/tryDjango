from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      'title',
      'description',
      'price'
    ]


class RawProductForm(forms.Form):
  title = forms.CharField(label='',widget=forms.TextInput(attrs={"placeholder":"your title"}))
  description = forms.CharField(
    required=False, 
    widget=forms.Textarea(
      attrs={
        "class":"new-class name",
        "rows":10,
        "cols":50,
        "id":"my_id"
      }
      )
      )
  price = forms.DecimalField(initial=199.99)