from django.shortcuts import render
# для связки с БД импортируем наш проект Project модуль
from .models import Project
# Create your views here.
def home(request):
    projects = Project.objects.all() # таким образом джанго импортирует все из БД
    return render(request, 'portfolio/home.html', {'projects':projects})