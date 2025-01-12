from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=25000000)
    date = models.DateField()

    def __str__(self): # для отображения в админской панели не номера проектов Project1... а нормально их заголовки
        return self.title