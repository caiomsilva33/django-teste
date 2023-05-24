from django.http import HttpResponse


def home(request):
    return HttpResponse('Ola Mundo')

def clientes(request):
    return HttpResponse('Cliente Todos')

def clientes_detalhes(request, id):
    return HttpResponse(f'Cliente Teste de ID {id}')

def cursos(request):
    return HttpResponse('Cursos')

def objetivos(request):
    return HttpResponse('Objetivos')