from captcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Incorrect login credentials. Please try again')
            return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password_conf = forms.CharField(max_length=150, widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_conf',
        ]

    def clean_password_conf(self):
        password = self.cleaned_data.get('password')
        password_conf = self.cleaned_data.get('password_conf')
        if password and password_conf and password != password_conf:
            raise forms.ValidationError('Passwords do not match')
        return password_conf
