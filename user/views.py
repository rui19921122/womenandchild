from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

from user.models import CustomUser
from .forms import RegisterForm, LoginForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid() and not request.user.is_authenticated():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                    username=data['nickname'],
                    password=data['password']
            )
            new = CustomUser(user=new_user, sex=data.get('sex'), phone=data.get('phone'))
            new.save()
            login(request, authenticate(username=new_user.username, password=data.get('password2')))
            return render(request, 'redirect.html', {'message': '感谢您的注册'})
        else:
            return render(request, 'register.html', {'form': form})
    elif request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, 'redirect.html', {'message': '您已登陆'})
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def login_url(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, 'redirect.html', {'message': '您已登陆'})
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['nickname'], password=data['password'])
            if user is not None:
                login(request, user)
                return render(request, 'redirect.html', {'message': '您已登陆成功'})
        else:
            return render(request, 'login.html', {'form': form})
