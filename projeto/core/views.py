from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required(login_url='/auth/login')
def index(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        return redirect('usuario:login')
