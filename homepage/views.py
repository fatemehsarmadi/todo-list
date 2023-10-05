from django.shortcuts import render, redirect
from .models import Task, Deadline
from .forms import TaskForm, DeadlineForm

def show_tasks(request):
    tasks = Task.objects.all().order_by('id').reverse()
    deadlines = Deadline.objects.all().order_by('priority')
    return render(request, 'index.html', {'tasks': tasks, 'deadlines': deadlines})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def toggle_task_status(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            task = Task.objects.get(id = task_id)
            task.is_done = not task.is_done
            task.save()
        except Task.DoesNotExist:
            pass
    return redirect('index')

def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        try:
            Task.objects.filter(id = task_id).delete()
        except Task.DoesNotExist:
            pass
    return redirect('index')

def update_task(request):
    if request.method == 'POST':
        form = TaskForm()
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id = task_id)
        context = {'form':form, 'task': task}
    return render(request, 'edit_page.html', context)

def save_update(request):
    task_id = request.POST.get('task_id')
    new_title = request.POST.get('new_title')
    task = Task.objects.get(id = task_id)
    task.title = new_title
    task.save()
    return redirect('index')

def add_deadline(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = Task.objects.all().get(id = task_id)
        form = DeadlineForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            priority = form.cleaned_data['priority']
            new_deadline = Deadline(date = date, description = description, priority = priority, task = task)
            new_deadline.save()
            return redirect('index')
        return render(request, 'deadline_page.html', {'form': form, 'task': task})