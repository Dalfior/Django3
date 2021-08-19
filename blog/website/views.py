from django.shortcuts import render
#Ler banco de dados
from .models import Post
#from django.http import HttpResponse

# Create your views here.

#def hello_blog(request):
#     return render(request, 'indexgeral.html')
#    #return HttpResponse('Blog')


def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git',
        'Html', 'Banco de Dados',
        'Linux', 'Nginx', 'Uwsgi',
        'Systemctl',
    ]
    list_posts = Post.objects.all()

    data = {
        'name': 'Curso de Django 3',
        'lista_tecnologias': lista,
        'posts': list_posts
    }
    return render(request, 'index.html', data)
    return HttpResponse('Blog')
