from django.shortcuts import render
from paginas.models import Usuario

# Create your views here.
def home(request):
    return render(request, 'index.html')

def ferramentas(request):
    return render(request, 'ferramentas.html')

def cursos(request):
    return render(request, 'cursos.html')

def fale_conosco(request):
  contexto = {'msg': ''}
  if request.method == 'POST':
    pessoa = Usuario()
    pessoa.nome = request.POST.get('nome')
    pessoa.email = request.POST.get('email')
    pessoa.comentario = request.POST.get('comentario')
    pessoa.save()
    contexto = {'msg': 'Sua dúvida/sugestão foi enviada com sucesso!'}
    return render(request, 'fale_conosco.html', contexto)
  return render(request, 'fale_conosco.html')