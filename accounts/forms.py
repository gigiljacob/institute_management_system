from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

ims_user = get_user_model()


class ImsUserCreationForm(UserCreationForm):

    class Meta:
        model = ims_user
        fields = ("email", "password1", "password2")


class ImsUserChangeForm(UserChangeForm):

    class Meta:
        model = ims_user
        fields = ("email",)
