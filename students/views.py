from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentRegistrationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def student_home(request):
    student = request.user
    return render(request, 'students/student_home.html', {'student': student})

def student_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_home')
        else:
            return render(request, 'students/student_login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'students/student_login.html')

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentRegistrationForm
    template_name = 'students/student_registration.html'
    success_url = reverse_lazy('student_list')
    login_url = '/login/'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentRegistrationForm
    template_name = 'students/student_registration.html'
    success_url = reverse_lazy('student_list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
