from django import forms
from .models import Breed,Cat

class BreedForm(forms.ModelForm):
    class Meta:
        model  = Breed
        fields = '__all__'

class CatForm(forms.ModelForm):
    class Meta:
        model  = Cat
        fields = '__all__'
  