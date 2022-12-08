from django import forms
from django.forms import widgets
"""Forms of the project."""

# Create your forms here.
class ThingForm(forms.Form):
    name= forms.CharField(widget=forms.Textarea)
    description= forms.CharField(widget=forms.Textarea)
    quantity= forms.IntegerField()
