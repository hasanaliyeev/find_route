from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.hashers import check_password

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'input username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'input password'
    }))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Wrong username')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Wrong password')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('User not active')
        return super().clean(*args, **kwargs)
