from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

# login page view
def home(request):
    return render(request, 'home.html', {})

# login page view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('admin_panel')  # Redirect authenticated users to the admin panel

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print(f"Attempting to log in user: {username}, password: {password}")  # Debugging

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # print(f"User authenticated: {user}")  # Debugging
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('admin_panel')
        else:
            # print("Authentication failed")  # Debugging
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'login.html')
  

# logout page view
def logout_view(request):
    logout(request)
    messages.success(request, '  You are now logged out')
    return redirect ('login')

# index.html function
def index_view(request):
    return render (request, 'index.html')

# Admin Panel view
def admin_panel_view(request):
    # Ensure only authenticated users can access this page
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to access the admin panel')
        return redirect('login')  # Redirect to login if not authenticated

    return render(request, 'admin_panel.html')