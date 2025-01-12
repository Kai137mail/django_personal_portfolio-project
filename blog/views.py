from django.shortcuts import render, get_object_or_404 # get_object это метод позволяющий отобразить нужную страницу или отобразить ошибку 404 если таковой нет
from .models import Blog
# Create your views here.
def all_blogs(request):
    blogs = Blog.objects.order_by('-date')#[:5] # так список блогов будет отсортирован по дате от новых к старым и ограничим кол-во выводимых записей =5 ([:5])
    return render(request, 'all_blogs.html', {'blogs':blogs})

def detail(request, blog_id): # здесь передаем не только запрос, но и переменную
    blog = get_object_or_404(Blog, pk=blog_id) # тут мы обращаемся к нашему cозданному классу Blog в БД, берем его primary key и приравниваем к переменной blog_id
    return render(request, 'detail.html', {'blog':blog})