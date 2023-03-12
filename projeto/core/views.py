from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .forms import FormTeste


@login_required(login_url='/auth/login')
def index(request):
    if request.method == 'GET':
        form = FormTeste()
        return render(request, 'home.html', {'form': form})
    else:

        form = FormTeste(request.POST)
        from django.forms.fields import CharField
        form.fields['num'] = CharField()

        return HttpResponse(form)
