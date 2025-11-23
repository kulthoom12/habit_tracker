from django.shortcuts import render, redirect
from .models import Task


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(
                title=title,
                user=request.user if request.user.is_authenticated else None
            )
        return redirect('home')

    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = Task.objects.all()

    return render(request, 'tasks/index.html', {'tasks': tasks})
