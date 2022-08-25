from socket import fromshare
from django import forms
from .models import AppUser, Product

class ProductCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        # fields = "__all__"    # if all fields are required
        fields = ('first_name', 'middle_name', 'last_name', 'email', 'password')
        model = AppUser
