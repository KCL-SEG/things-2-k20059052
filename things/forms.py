from django import forms
from django.forms import widgets
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields =["name","description","quantity"]
        widgets ={"name": forms.Textarea(), "quantity": forms.NumberInput(), "description":forms.Textarea()}

    #name= forms.CharField(widget=forms.Textarea, max_length =35)
    #description= forms.CharField(widget=forms.Textarea, max_length=120)
    #quantity= forms.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(50)])
