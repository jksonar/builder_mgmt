from django.shortcuts import render, redirect
from users.forms import UserForm
from users.models import User

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})