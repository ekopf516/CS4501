from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import user, book
from django.contrib.auth import hashers


class UserForm(forms.ModelForm):
    class Meta:
        model = user
        exclude = ['bag']

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        exclude = []


class authenticate_form(forms.Form):
    authenticator = forms.CharField(max_length=900)