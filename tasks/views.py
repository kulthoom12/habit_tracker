from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
  if request.user.is_authenticated:
    else:


tasks = Task.objects.all()
return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    if request.method == "POST":
        title = request.POST.get("title")

        if title != "";
           Task.objects.create(
              user=request.user if request.user.is_authenticated
              else None,
              title=title)
           return redirect("task_list")
        return render(request, "tasks/task_form.html")


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
return render(request, "tasks/task_form.html", {"task": task})

def task_delete(request, pk):
      task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("task_list")

def clear_completed(request):
     done_tasks = Task.objects.filter(completed=True)
    done_tasks.delete()
return redirect("task_list")