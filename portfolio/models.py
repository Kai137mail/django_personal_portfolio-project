from django.db import models

# Create your models here.
# создаем новый класс Project наследника от Model из библиотеки models со следующими атрибутами
# типы полей атрибутов можно посмотреть на https://django.fun/docs/django/5.0/ref/models/fields/
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
# после внесенных изменений в этом файле питон выдаст предупреждение о миграциях
# ВАЖНО! нужно выполнить команду python3 manage.py makemigrations для применения изменений в БД нашего проекта
# и команду python3 manage.py migrate для применения изменений всех оставшихся стандартных библиотек
    def __str__(self): # для отображения в админской панели не номера проектов Project1... а нормально их заголовки
        return self.title