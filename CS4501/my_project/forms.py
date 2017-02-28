from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import user, book


class UserForm(forms.ModelForm):
    class Meta:
        model = user
        exclude = ['bag']

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        exclude = []