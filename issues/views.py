from django.shortcuts import render, redirect
from issues.forms import IssueForm
from issues.models import Issue

def report_issue(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
    else:
        form = IssueForm()
    return render(request, 'issues/report_issue.html', {'form': form})


def issue_list(request):
    issues = Issue.objects.all()
    return render(request, 'issues/issue_list.html', {'issues': issues})