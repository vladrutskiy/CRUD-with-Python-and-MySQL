from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    pass