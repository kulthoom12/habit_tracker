from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()

    return render(request, "tasks/login.html", {"form": form})


def habit_list(request):
    if not request.user.is_authenticated:
        return redirect('login')  

    habits = Habit.objects.filter(user=request.user)  
    return render(request, "tasks/index.html", {"habits": habits}) 


def habit_create(request):
    if not request.user.is_authenticated:
        return redirect('login')  

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        frequency = request.POST.get("frequency")
        completed_today = 'completed_today' in request.POST
        
        Habit.objects.create(
            user=request.user,
            title=title,
            description=description,
            frequency=frequency,
            completed_today=completed_today
        )
        return redirect("habit_list")

    return render(request, "tasks/form.html")


def habit_update(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    habit = get_object_or_404(Habit, id=pk)
    if habit.user != request.user:
        return redirect('habit_list')

    if request.method == "POST":
        habit.title = request.POST.get("title")
        habit.completed_today = 'completed_today' in request.POST
        habit.frequency = request.POST.get("frequency")

        if habit.completed_today:
            habit.streak += 1
        else:
            habit.streak = 0
        
        habit.save() 
        return redirect("habit_list") 

    return render(request, "tasks/form.html", {"habit": habit}) 


def habit_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')

    habit = get_object_or_404(Habit, id=pk) 
    if habit.user != request.user:
        return redirect("habit_list")

    habit.delete() 
    return redirect("habit_list") 


def clear_completed(request):
    if not request.user.is_authenticated:
        return redirect('login')

    Habit.objects.filter(user=request.user, completed_today=True).delete() 
    return redirect("habit_list")
