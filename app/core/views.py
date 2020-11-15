
from django.shortcuts import render, redirect
from core.forms import ComputadoraForm
from core.models import Computadora

# Create your views here.
def home(request):
    if request.method == "POST":
        form = ComputadoraForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = ComputadoraForm()
    return render(request, "index.html", {'form': form})

def show(request):
    computador = Computadora.objects.all()
    return render(request, "show.html", {'computadora': computador})

def edit(request, id):
    computador = Computadora.objects.get(id = id)
    return render(request, "edit.html", {'computadora': computador})

def update(request, id):
    computador = Computadora.objects.get(id = id)
    form = ComputadoraForm(request.POST, instance = computador)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {'computadora': computador})

def delete(request, id):
    computador = Computadora.objects.get(id = id)
    computador.delete()
    return redirect("/show")