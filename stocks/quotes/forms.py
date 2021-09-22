from django import forms
from .models import Stock

class stockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["ticker"]
