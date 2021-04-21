from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    #return HttpResponse("Hello, world. You're at the account index.")
    return render(request, 'comptes/pages/index.html', locals())

def login(request):
    #return HttpResponse("Hello, world. You're at the account index.")
    return render(request, 'comptes/pages/login.html', locals())

