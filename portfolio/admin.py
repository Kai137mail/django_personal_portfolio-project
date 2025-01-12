from django.contrib import admin
# для создания суперюзера в админской панели используем команду python3 manage.py createsuperuser и далее создаем имя и пароль
# для управления в админской панели нашим проектом импортируем из .models наш созданный класс Project
from .models import Project
# прописываем это для того, чтобы увидеть наш проект в админской панели
admin.site.register(Project)