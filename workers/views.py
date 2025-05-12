from django.shortcuts import render, redirect
from workers.forms import WorkerForm
from workers.models import Worker

def create_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'workers/create_worker.html', {'form': form})


def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'workers/worker_list.html', {'workers': workers})

