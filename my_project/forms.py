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
# class UserForm(forms.ModelForm):
#    class Meta:
#        model = user
#        fields = ('first_name', 'last_name', 'user_name','password')
#        firstName = forms.CharField(label='First Name', min_length=4, max_length=20)
#        lastName = forms.CharField(label='Last Name', min_length=4, max_length=30)
#        userName = forms.CharField(label='Username', min_length=4, max_length=30)
#        password = forms.CharField(label='Password', min_length=8, max_length=16)
# class BookForm(forms.ModelForm):
#    class Meta:
#        model = book
#        fields = ('title', 'author', 'isbn_num')
#        book_title = forms.CharField(label='Title', min_length=4, max_length=30)
#        book_author = forms.CharField(label='Author', min_length=4, max_length=100)
#        isbn = forms.CharField(label='ISBN Number', min_length = 10, max_length=10)


class UserForm(forms.ModelForm):
    firstName = forms.CharField(label='First Name', min_length=4, max_length=20)
    lastName = forms.CharField(label='Last Name', min_length=4, max_length=30)
    userName = forms.CharField(label='Username', min_length=4, max_length=30)
    password = forms.CharField(label='Password', min_length=8, max_length=16)
    def userName_clean(self):
        return self.cleaned_data['userName']
    def password_clean(self):
        return self.cleaned_data['password']
    def firstName_clean(self):
        return self.cleaned_data['fistName']
    def lastName_clean(self):
        return self.cleaned_data['lastName']