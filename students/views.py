from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm
from .models import Student

def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # user.username = form.cleaned_data['email']
            user.save()
            student = Student(user=user, **form.cleaned_data)
            student.save()
            login(request, user)
            return redirect('students:home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'students/register.html', {'form': form})

def home(request):
    student = Student.objects.get(user=request.user)
    return render(request, 'students/home.html', {'student': student})