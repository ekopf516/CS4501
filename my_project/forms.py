from django import forms
from .models import user

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('first_name', 'last_name', 'user_name','password')
