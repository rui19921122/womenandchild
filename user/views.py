from django.shortcuts import render

from .forms import RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
        # todo complete
