from django import forms

from .models import Proveedor

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model = Proveedor
        exclude = ['um','fm','uc','fc']
        widget = {'descripcion': forms.TextInput()}
    
    def __init__(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].wiget.attrs.update({
                'class':'form-control'
            })