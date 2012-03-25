from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_page(request):
    if request.user.is_authenticated():
        return redirect('/')
    if not request.POST:
        return render(request, 'registration/login.html', {})

    # else login the user
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user:
        if user.is_active:
            login(request, user)
            return redirect('/')
        else:
            # user is disabled
            return render(request, 'registration/login.html', { 'errors': 'This account is disabled' })
    else:
        # bad username/password
        return render(request, 'registration/login.html', { 'errors': 'Username and password do not match' })

def logout_page(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('/accounts/login/')

def register(request):
    return redirect('/')
