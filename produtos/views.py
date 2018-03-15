from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    descricao = "Ola Mundo"
    numero = 20 + 30
    return render(request,"produtos/home.html",{"des":descricao, "num": numero})

def paginaLogin(request):
    return render(request,'produtos/login.html')
