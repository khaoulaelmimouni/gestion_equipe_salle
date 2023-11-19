from django.shortcuts import render, redirect,get_object_or_404
from .models import Equipe, salle
from .forms import EquipeForm, salleForm

# Create your views here.

def data_list(request):
    equipess = Equipe.objects.all()
    salles = salle.objects.all()
    return render(request, 'playground/data_list.html', {'equipes': equipess, 'salles': salles})

def detail_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    return render(request, 'playground/detail_equipe.html', {'equipe': equipe})

def detail_salle(request, id_salle):
    sallee = get_object_or_404(salle, id_salle=id_salle)
    return render(request, 'playground/detail_salle.html', {'salle': sallee})

def create_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST,  request.FILES)
        if form.is_valid():
            equipe = form.save()
            return redirect('detail_equipe', id_equipe=equipe.id_equipe)  
    else:
        form = EquipeForm()

    return render(request, 'playground/create_equipe.html', {'form': form})

def create_salle(request):
    if request.method == 'POST':
        form = salleForm(request.POST, request.FILES)
        if form.is_valid():
            salle = form.save()
            return redirect('detail_salle', id_salle=salle.id_salle) 
    else:
        form = salleForm()

    return render(request, 'playground/create_salle.html', {'form': form})

def delete_salle(request, id_salle):
    sallee = get_object_or_404(salle, id_salle=id_salle)
    sallee.delete()
    return redirect('data_list')

def delete_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    equipe.delete()
    return redirect('data_list')

def modify_equipe(request, id_equipe):
    equipe = get_object_or_404(Equipe, id_equipe=id_equipe)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('detail_equipe', id_equipe=id_equipe)
    else:
        form = EquipeForm(instance=equipe)
    
    return render(request, 'playground/modify_equipe.html', {'form': form, 'equipe': equipe})


def modify_salle(request, id_salle):
    sallee = get_object_or_404(salle, id_salle=id_salle)
    if request.method == 'POST':
        form = salleForm(request.POST, request.FILES, instance=sallee)
        if form.is_valid():
            form.save()
            return redirect('detail_salle', id_salle=id_salle)  
    else:
        form = salleForm(instance=sallee)

    return render(request, 'playground/modify_salle.html', {'form': form})