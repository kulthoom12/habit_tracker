from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect


def redirect_to_login(request):
    return redirect('login')


urlpatterns = [
    path('', redirect_to_login, name='root'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('habits/add/', views.habit_form, name='habits_create'),
    path('habits/edit/<int:pk>/', views.habit_form, name='habits_update'),
    path('habits/delete/<int:pk>/', views.habits_delete, name='habits_delete'),

    path('habits/toggle/<int:pk>/', views.toggle_completed, name='habit_toggle'),
]
