from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def ferramentas(request):
    return render(request, 'ferramentas.html')

def cursos(request):
    return render(request, 'cursos.html')

def fale_conosco(request):
    return render(request, 'fale_conosco.html')