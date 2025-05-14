from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from builders.forms import BuilderForm, BuilderCompanyForm
from builders.models import Builder, BuilderCompany

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
def create_builder_company(request):
    if request.user.user_type != 'builder':
        messages.error(request, "Only builders can create company profiles.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = BuilderCompanyForm(request.POST)
        if form.is_valid():
            company = form.save(commit=False)
            company.contact_person = request.user
            company.save()
            messages.success(request, 'Builder company created successfully!')
            return redirect('builder_company_list')
    else:
        form = BuilderCompanyForm()
    
    return render(request, 'builders/create_builder_company.html', {'form': form})

@login_required
def builder_company_list(request):
    if request.user.user_type == 'admin':
        companies = BuilderCompany.objects.all()
    else:
        companies = BuilderCompany.objects.filter(contact_person=request.user)
    return render(request, 'builders/builder_company_list.html', {'companies': companies})

@login_required
def edit_builder_company(request, pk):
    company = get_object_or_404(BuilderCompany, pk=pk)
    
    if request.user != company.contact_person and request.user.user_type != 'admin':
        messages.error(request, "You don't have permission to edit this company.")
        return redirect('builder_company_list')
    
    if request.method == 'POST':
        form = BuilderCompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company details updated successfully!')
            return redirect('builder_company_list')
    else:
        form = BuilderCompanyForm(instance=company)
    
    return render(request, 'builders/edit_builder_company.html', {
        'form': form,
        'company': company
    })

@login_required
def builder_list(request):
    # If user is admin, show all builders
    if request.user.user_type == 'admin':
        builders = Builder.objects.all()
    else:
        # Show only the builder's own details
        builders = Builder.objects.filter(user=request.user)
    return render(request, 'builders/builder_list.html', {'builders': builders})