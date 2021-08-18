from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def hello_blog(request):
    return render(request, 'indexgeral.html')
    #return HttpResponse('Blog')
