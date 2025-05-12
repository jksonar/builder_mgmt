from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from builders.models import Builder
from projects.models import Project
from workers.models import Worker
from tasks.models import Task

@login_required
def dashboard_view(request):
    context = {
        'total_builders': Builder.objects.count(),
        'total_projects': Project.objects.count(),
        'total_workers': Worker.objects.count(),
        'pending_tasks': Task.objects.filter(status='Pending').count(),
    }
    return render(request, 'dashboard/dashboard.html', context)
