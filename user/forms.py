from django import forms
from django.core.exceptions import ValidationError
from localflavor.cn.forms import CNPhoneNumberField


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=10, label='姓名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(max_length=10, min_length=3, label='昵称',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(choices=(('m', '男'), ('f', '女')), label='性别',
                            widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=10, min_length=6, label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=10, min_length=6, label='重复密码',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = CNPhoneNumberField(label='手机号码', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birthday = forms.DateField(label='生日', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_password2(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password2 != password1:
            raise ValidationError('两个密码不一致', code='invalid')
