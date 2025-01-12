from django.urls import path
# можем вместо папки откуда импортируем можем просто написать . потому что файл находится в этой же папке
from . import views

app_name = 'blog' # это переменная для уточнения чтобы идти сюда из страницы all_blogs.html
urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    # path('3', views.detail, name='detail'), # создадим отдельную страницу для конкретного блога №3. Но это неудобно т.к. страниц может быть много
    path('<int:blog_id>/', views.detail, name='detail'), # поэтому создадим такую конструкцию. Она принимает в себя любую страницу по blog_id. int указывает на то какого типа придет значение, это может быть и str
]
