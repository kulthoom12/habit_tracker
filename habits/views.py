from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import HabitForm
from .models import Habit

def redirect_to_login(request):  
    if request.user.is_authenticated:  
        return redirect('home') 
    return redirect('login')  


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Registration successful! You are now logged in.")
            return redirect('home')
        else:
            messages.error(
                request, "There was an error with your registration.")
    else:
        form = UserCreationForm()
    return render(request, "habits/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials.")
    else:
        form = AuthenticationForm()
    return render(request, "habits/login.html", {"form": form})


#  login_required
@login_required
def home(request):
    if not request.user.is_authenticated:
          return redirect('login')
    habits = Habit.objects.filter(user=request.user).order_by('-id')
    return render(request, "habits/index.html", {"habits": habits})

@login_required
def habit_form(request, pk=None):
    habit = None
    if pk:
        habit = get_object_or_404(Habit, id=pk, user=request.user)

    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.update_streak()
            habit.save()
            messages.success(request, "Habit saved successfully.")
            return redirect("home")
        else:
            messages.error(request, "There was an error saving the habit.")
    else:
        form = HabitForm(instance=habit)

    return render(request, "habits/form.html", {"form": form, "habit": habit})


@login_required
def habits_delete(request, pk):
    habit = get_object_or_404(Habit, id=pk, user=request.user)
    habit.delete()
    messages.success(request, "Habit deleted successfully.")
    return redirect("home")


@login_required
def habits_clear_completed(request):
    Habit.objects.filter(user=request.user, completed_today=True).delete()
    messages.success(request, "Completed habits cleared successfully.")
    return redirect("home")
