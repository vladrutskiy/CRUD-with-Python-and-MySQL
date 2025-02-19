from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.

# Homepage view
def home(request):
    # checking the user is logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user authentication
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            # redirecting the user to page
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# login page view
# def login_view(request):
#     pass

# logout page view
def logout_view(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect ('home')

# creating registration view/function
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Auth and login user right away
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, 'You are successfully registered and welcome to Calgary Music')
            return redirect ('home')
        else:
            messages.error(request, 'There was an error with your registration, please correct the errors')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})