from django.shortcuts import render,  get_object_or_404
from .models import Titulo, Novidade

def index(request):
    '''Página principal do noticias.'''
    return render(request, 'noticias/index.html')

def titulos(request):
    '''Mostra todos os títulos(Assuntos).'''
    titulos = Titulo.objects.order_by('date_added')
    context = {'titulos':titulos}
    return render(request, 'noticias/noticias.html', context)

def corpo(request, titulo_id):
    """Exibe o título e seus corpos associados.

    Args:
        request: Objeto de requisição HTTP.
        titulo_id: ID do título a ser exibido.

    Returns:
        HttpResponse: Renderiza o template 'noticias/topic.html' com o contexto.
    """

    titulo = get_object_or_404(Titulo, id=titulo_id)
    corpos = titulo.corpo_set.order_by('-date_added')
    context = {'titulo': titulo, 'corpos': corpos}
    return render(request, 'noticias/artigos.html', context)

def novidades(request):
    novidades = Novidade.objects.order_by('-data_criacao')
    context = {'novidades': novidades}
    return render(request, 'noticias/novidades.html', context)

def clima(request):
    return render(request, 'noticias/clima.html')