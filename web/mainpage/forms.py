from django import forms

class user_info(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class login_form(forms.Form):
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class book_info(forms.Form):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    publisher = forms.CharField(max_length=200)
    isbn_num = forms.CharField(max_length=10)
    price = forms.IntegerField()
    pub_date = forms.DateField()