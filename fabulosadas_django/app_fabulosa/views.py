from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PropRetos, Retos
from .forms import FormRetos

# Create your views here.
def index(request):
    return render(request, 'index.html')

def retos(request):
    retos = Retos.objects
    if request.method == 'GET':
        return render(request, 'RetosFabulosos.html', {
            'form': FormRetos(),
            'retos': retos,
        })
    else:
        form = FormRetos(request.POST)
        if form.is_valid():
            retos.create(username=request.POST['username'], reto_name=request.POST['reto_name'], difficulty=request.POST['difficulty'], description=request.POST['description'], gmail=request.POST['gmail'])
            return redirect('index')
