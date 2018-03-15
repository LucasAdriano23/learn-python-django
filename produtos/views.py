from django.shortcuts import render, HttpResponse

# Create your views here.

def paginaInicial(request):
    return HttpResponse("Bem vindo a pagina do app de produtos")

def paginaLogin(request):
    return HttpResponse("Pagina de Login!")
