from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, max_length = 30, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(required = True, max_length = 30, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(required = True, max_length = 30, label = '', widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        # to add all fields 
        # fileds = '__all__'
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # some rules for the form
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'