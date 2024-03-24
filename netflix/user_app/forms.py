from django import forms
from netflix_app.models import *

class UserForm(forms.ModelForm):

    email = forms.CharField(label="",widget=forms.EmailInput(attrs={"placeholder": "E-mail Adresi"}))  
    username = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"placeholder": "Sifreniz"}))

    class Meta:
        model = NetflixUser
        fields = ["email","username","password"]

        # help_texts = {
        #     'username': None,
        #     'password': None
        # }

        # labels = {

        #     'username': "",
        #     'password': ""
        # }


class ProfileForm(forms.ModelForm):

    class Meta:
        model = NetflixProfile
        fields = ["name","avatar"]