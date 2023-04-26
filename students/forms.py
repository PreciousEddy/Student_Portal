from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'phone', 'address_1', 'address_2', 'password1', 'password2')