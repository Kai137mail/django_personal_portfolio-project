"""
URL configuration for personal_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# для того чтобы работали ссылки на наши изображения в проекте добавим
from django.conf.urls.static import static

# импортируем файл с настройками, чтобы из него можно было взять переменную MEDIA_URL для нашего пути к файлам с изображениями
from django.conf import settings

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # не забывает импортировать метод include в from django.urls
    path('blog/', include('blog.urls')),
]

# добавим статический путь для наших изображений в проекте.
# Это адрес от куда будут прикрепляться изображения к нашим проектам
# и в нем укажем переменную из settings.py MEDIA_URL и конкретный каталог MEDIA_ROOT
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
