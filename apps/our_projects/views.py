from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import OurProjects
from .forms import CardProjectForm

def our_projects(request):
    # Получаем все проекты из базы данных
    projects = OurProjects.objects.all().order_by('-id')

    # Проверяем, является ли пользователь staff (админ или модератор)
    is_staff_user = request.user.is_authenticated and request.user.is_staff

    if request.method == 'POST' and is_staff_user:
        form = CardProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Проект успешно добавлен!")
            return redirect('our_projects:our_projects')
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = CardProjectForm() if is_staff_user else None

    context = {
        'projects': projects,
        'form': form,
        'is_staff_user': is_staff_user,
        'is_authenticated': request.user.is_authenticated
    }
    return render(request, 'our_projects.html', context)


# View для отдельной страницы добавления
@login_required
def add_project(request):
    if not request.user.is_staff:
        messages.error(request, "У вас нет прав для добавления проектов.")
        return redirect('our_projects:our_projects')

    if request.method == 'POST':
        form = CardProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Проект успешно добавлен!")
            return redirect('our_projects:our_projects')
    else:
        form = CardProjectForm()

    context = {
        'form': form
    }
    return render(request, 'add_project.html', context)