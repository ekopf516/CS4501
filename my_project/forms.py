from django import forms
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import user, book

#class UserCreate(CreateView):
#   model = user
#   fields = ['first_name', 'last_name', 'user_name', 'password']

#class BookCreate(CreateView):
#   model = book
#   fields = ['title', 'author', 'publisher', 'pub_date','isbn_num', 'price']


# Code from django website tutorial
class UserForm(forms.ModelForm):
   class Meta:
       model = user
       fields = ('first_name', 'last_name', 'user_name','password')
       firstName = forms.Charfield(label='First Name', min_length=4, max_length=20)
       lastName = forms.Charfield(label='Last Name', min_length=4, max_length=30)
       userName = forms.Charfield(label='Username', min_length=4, max_length=30)
       password = forms.Charfield(label='Password', min_length=8, max_length=16)
class BookForm(forms.ModelForm):
   class Meta:
       model = book
       fields = ('title', 'author', 'isbn_num')
       book_title = forms.Charfield(label='Title', min_length=4, max_length=30)
       book_author = forms.Charfield(label='Author', min_length=4, max_length=100)
       isbn = forms.Charfield(label='ISBN Number', min_length = 10, max_length=10)