from django.shortcuts import render, redirect
from .models import task
from .form import taskForm

# def task_list(request):
#     tasks=task.objects.all()
#     return render(request, 'task_list.html', {'tasks': tasks})


def task_list(request):
    form=taskForm()
    tasks=task.objects.all()
    if request.method=='POST':
        form=taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    
    return render(request, 'task_list.html', {'form': form,'tasks':tasks})


def update_task(request, id):
    t=task.objects.get(id=id)
    if request.method=='POST':
        form=taskForm(request.POST,instance=t)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form=taskForm(instance=t)
    return render(request,'update_task.html',{'form': form})


def delete_task(request, id):
    task.objects.filter(id=id).delete()
    return redirect('task')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')
