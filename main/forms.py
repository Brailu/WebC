from django import forms
from main.models import Calculator


class CalculatorForm(forms.ModelForm):
    
    class Meta:
        model = Calculator
        fields = ["name"]
