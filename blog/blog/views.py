from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello worlds")

def index_home(request):
    return HttpResponse("Testando pagina de index")