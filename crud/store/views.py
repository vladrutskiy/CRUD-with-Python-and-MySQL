from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Persons
from .forms import RegistrationForm


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
    persons = Persons.objects.all()
    # Ensure only authenticated users can access this page
    if not request.user.is_authenticated:
        messages.error(request, 'You must be logged in to access the Admin Panel')
        return redirect('login')  # Redirect to login if not authenticated
    # else: 
    #     return render (request)

    

    return render(request, 'admin_panel.html', {'persons': persons})

def person(request, pk):
    if  request.user.is_authenticated:
        # searching for a specific person
        person_record = Persons.objects.get(PersonID = pk)
        return render(request, 'person.html', {'person_record': person_record})
    else:
         messages.error(request, 'You must be logged in to access the Admin Panel')
         return redirect('login')  # Redirect to login if not authenticated

# delete a person form a list
def person_delete(request, pk):
    if  request.user.is_authenticated:
        delete_record = Persons.objects.get(PersonID = pk)
        delete_record.delete()
        messages.success(request, "You have successfully deleted…")
        return redirect('admin_panel')
    else:
        messages.error(request, 'You must be logged in to access the Admin Panel')
        return redirect('login')  # Redirect to login if not authenticated
    

# creating registration an admin user view/function
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
            return redirect ('admin_panel')
        else:
            messages.error(request, 'There was an error with your registration, please correct the errors')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})  
  


# Add a person from UI
def person_add_view(request):
    return render(request, 'person_add.html', {})
