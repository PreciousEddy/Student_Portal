from django.urls import path
from .views import StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView, student_login, student_home

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('registration/', StudentCreateView.as_view(), name='student_registration'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
    path('login/', student_login, name='student_login.html'),
    path('home/', student_home, name='student_home'),
]
