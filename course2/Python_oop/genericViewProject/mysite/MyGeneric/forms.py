from django import forms 
from .models import Book

class BookForm(forms.ModelForm):
    publication_date = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Book
        fields = "__all__"
    

