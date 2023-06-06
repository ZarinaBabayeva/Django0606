from django import forms
from app.models import Product

class ProductForm(forms.ModelForm):
    tax_price = forms.FloatField()

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'discount_price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':f"{field} form-control"})

    def clean(self):
        price = self.cleaned_data.get('price')
        discount_price = self.cleaned_data.get('discount_price')
        tax_price = self.cleaned_data.get('tax_price')
        if price-(discount_price+tax_price) == 0:
            raise forms.ValidationError("Price Tax Price ile Discount Price-in ferqinden boyuk olmalidir.")
        return super().clean()
    def save(self,commit=True):
        self.cleaned_data["name"] = self.cleaned_data["name"].upper()
        if commit:
            del self.cleaned_data["tax_price"]
            return Product.objects.create(**self.cleaned_data)
        else :
            return Product(**self.cleaned_data)