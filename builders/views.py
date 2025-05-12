from django.shortcuts import render, redirect
from builders.forms import BuilderForm
from builders.models import Builder

def create_builder(request):
    if request.method == 'POST':
        form = BuilderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('builder_list')
    else:
        form = BuilderForm()
    return render(request, 'builders/create_builder.html', {'form': form})

def builder_list(request):
    builders = Builder.objects.all()
    return render(request, 'builders/builder_list.html', {'builders': builders})