from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from localflavor.cn.forms import CNCellNumberField


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=10, label='姓名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(max_length=10, min_length=3, label='昵称',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(choices=(('m', '男'), ('f', '女')), label='性别',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=10, min_length=6, label='密码',
                               widget=forms.PasswordInput(
                                       attrs={'class': 'form-control', 'placeholder': '请输入6-10位的密码'}))
    password2 = forms.CharField(max_length=10, min_length=6, label='重复密码',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = CNCellNumberField(label='手机号码', widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise ValidationError('两个密码不一致', code='invalid')
        return self.cleaned_data.get('password2')

    def clean_nickname(self):
        if User.objects.filter(username=self.cleaned_data.get('nickname')).exists():
            raise ValidationError('该用户名已被注册，请重新输入,或者<a href="/login">登陆<a/>', code='invalid')
        return self.cleaned_data.get('nickname')


class LoginForm(forms.Form):
    nickname = forms.CharField(max_length=10, min_length=3, label='昵称',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_password(self):
        nickname = self.cleaned_data.get('nickname')
        password = self.cleaned_data.get('password')
        if not authenticate(username=nickname, password=password):
            raise ValidationError("错误的用户名或密码", code='invalid')
        return password
