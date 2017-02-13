from django import forms
from .models import user, book

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('first_name', 'last_name', 'user_name','password')

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ('title', 'author', 'isbn_num')