from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is Home Page</h1>")

def login(request):
    return HttpResponse("<h1>This is Login Page</h1>")

def blog(request):
    return HttpResponse("<h1>This is Blog Page</h1>")