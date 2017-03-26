from django import forms

class login_form(forms.Form):
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class user_info(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    user_name = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

class authenticate_form(forms.Form):
    authenticator = forms.CharField(max_length=900)