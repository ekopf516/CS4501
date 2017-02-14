from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import user, book
#move to views.py when it is updated

class UserCreate(CreateView):
    model = user
    fields = ['first_name', 'last_name', 'user_name', 'password']

class BookCreate(CreateView):
    model = book
    fields = ['title', 'author', 'publisher', 'pub_date','isbn_num', 'price']


# Code from django website tutorial
#class UserForm(forms.ModelForm):
#   class Meta:
#       model = user
#       fields = ('first_name', 'last_name', 'user_name','password')

#class BookForm(forms.ModelForm):
#   class Meta:
#       model = book
#       fields = ('title', 'author', 'isbn_num')