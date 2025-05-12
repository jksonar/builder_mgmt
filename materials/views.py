from django.shortcuts import render, redirect
from materials.forms import MaterialForm
from materials.models import Material

def create_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'materials/create_material.html', {'form': form})


def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})