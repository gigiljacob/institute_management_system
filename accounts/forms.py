from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

ims_user = get_user_model()


class ImsUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput,)
    password2 = forms.CharField(label="Confirm Password", strip=False, widget=forms.PasswordInput)

    class Meta:
        model = ims_user
        fields = ("first_name", "last_name", "email", "phone")


class ImsUserChangeForm(UserChangeForm):

    class Meta:
        model = ims_user
        fields = ("email",)
