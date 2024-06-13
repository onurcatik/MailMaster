# forms.py
from django import forms
from .models import Person, Recipient

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email']

class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'email']
