from django.contrib import admin
from .models import Blog
# Register your models here.

# прописываем это для того, чтобы увидеть наш проект в админской панели
admin.site.register(Blog)