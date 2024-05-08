from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Login", widget=forms.TextInput(attrs={}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={}))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat Password", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        label = {
            'email': 'E-Mail',
            'first_name': 'Name',
            'last_name': "Surname",
            'password': 'Password',
            'password2': 'Repeat Password'
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password == password2:
            raise forms.ValidationError("Passwords don't match!")
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This e-mail already exists!')
        return email
