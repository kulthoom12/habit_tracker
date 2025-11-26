from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Task

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

def task_list(request):
    if not request.user.is_authenticated:  
        return redirect('login')  

    tasks = Task.objects.filter(user=request.user)  
    return render(request, "tasks/index.html", {"tasks": tasks})

def task_create(request):
    if not request.user.is_authenticated:  
        return redirect('login')  

    if request.method == "POST":
        title = request.POST.get("title")
        if title != "":
            Task.objects.create(
                user=request.user,  
                title=title
            )
        return redirect("task_list")  

    return render(request, "tasks/form.html")  

def task_update(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.title = request.POST.get("title")
        if request.POST.get("completed") == "on":
            task.completed = True
        else:
            task.completed = False
        task.save()
        return redirect("task_list")
    return render(request, "tasks/form.html", {"task": task})


def task_delete(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("task_list")


def clear_completed(request):
    done_tasks = Task.objects.filter(completed=True)
    done_tasks.delete()
    return redirect("task_list")
