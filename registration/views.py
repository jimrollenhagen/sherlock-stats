from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from registration.models import UserProfile

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
    if request.user.is_authenticated():
        return redirect('/')
    if not request.POST:
        return render(request, 'registration/register.html', {})

    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['password2']
    what_username = request.POST['what-username']

    errors = []
    # verify what.cd username not in use
    dupe_user = UserProfile.objects.filter(whatcd_username=what_username).count()
    if dupe_user:
        errors.append('What.CD user %s already has a sherlock account' % what_username)

    # verify passwords match
    if password != password2:
        errors.append('Passwords do not match')
    # verify password security
    if len(password) < 8:
        errors.append('Passwords must be at least 8 characters')

    # verify username valid and not taken
    if not username:
        errors.append('Username cannot be empty')
    dupe_user = User.objects.filter(username=username).count()
    if dupe_user:
        errors.append('Username already taken')

    # TODO
    # verify user with what.cd and get ID
    # do this last so we don't make HTTP requests if not necessary
    what_id = 154963

    # return any errors
    if errors:
        errors = '. '.join(errors)
        return render(request, 'registration/register.html', {'errors': errors, 'username': username, 'what_username': what_username})

    # register account
    user = User(username=username, password=password)
    user.save()
    profile = UserProfile(user=user, whatcd_username=what_username, whatcd_id=what_id)
    profile.save()

    # TODO generate verification key, do verification logic

    # TODO send PM to what.cd account
    # return register successful
    return render(request, 'registration/register_success.html', {})
