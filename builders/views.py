from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from builders.forms import BuilderForm
from builders.models import Builder

@login_required
def create_builder(request):
    if request.method == 'POST':
        form = BuilderForm(request.POST)
        if form.is_valid():
            builder = form.save(commit=False)
            builder.user = request.user
            builder.save()
            return redirect('builder_list')
    else:
        form = BuilderForm()
    return render(request, 'builders/create_builder.html', {'form': form})

@login_required
def builder_list(request):
    # If user is admin, show all builders
    if request.user.user_type == 'admin':
        builders = Builder.objects.all()
    else:
        # Show only the builder's own details
        builders = Builder.objects.filter(user=request.user)
    return render(request, 'builders/builder_list.html', {'builders': builders})