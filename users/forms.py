
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField

user = get_user_model()

class UserModelForm(forms.ModelForm):
    class Meta:
        model = user
        fields = (
            'username',
            'email',
            'address'
        )


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(label='Email')

    error_messages ={
            'invalid_login' : "Invalid Credentials"
        }


class SignupForm(UserCreationForm):
    class Meta:
        model = user
        fields = (
            'username',
            'email',
            'address'
        )

        field_classes = {'username' : UsernameField}