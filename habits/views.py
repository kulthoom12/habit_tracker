from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from .forms import HabitForm

# Register View


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, "habits/register.html", {"form": form})

# Login View


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, "habits/login.html", {"form": form})

# Habit List View


def habits_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    habits = Habit.objects.filter(user=request.user)
    return render(request, "habits/index.html", {"habits": habits})

# Habit Create & Update View


def habit_form(request, pk=None):
    if not request.user.is_authenticated:
        return redirect('login')

    if pk:
        habit = get_object_or_404(Habit, id=pk, user=request.user)
    else:
        habit = None

    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user

            if habit.completed_today:
                habit.streak += 1
            else:
                habit.streak = 0

            habit.save()
            return redirect("habits_list")

    else:
        form = HabitForm(instance=habit)

    return render(request, "habits/form.html", {"form": form, "habit": habit})


def habits_update(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    habit = get_object_or_404(Habit, id=pk)
    if habit.user != request.user:
        return redirect("habits_list")

    if request.method == "POST":
        habit.title = request.POST.get("title")
        habit.completed_today = 'completed_today' in request.POST
        habit.frequency = request.POST.get("frequency")

        if habit.completed_today:
            habit.streak += 1
        else:
            habit.streak = 0

        habit.save()
        return redirect("habits_list")

    return render(request, "habits/form.html", {"habit": habit})

# Habit Delete View


def habits_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    habit = get_object_or_404(Habit, id=pk, user=request.user)
    habit.delete()
    return redirect("habits_list")

# Clear Completed Habits


def habits_clear_completed(request):
    if not request.user.is_authenticated:
        return redirect('login')

    Habit.objects.filter(user=request.user, completed_today=True).delete()
    return redirect("habits_list")
