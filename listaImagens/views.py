from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from .models import Imagens

def index(request):    
    imagens_list = Imagens.objects.all()
    paginator = Paginator(imagens_list, 33)  # Crie um Paginator, 10 imagens por página

    page_number = request.GET.get('page')
    imagens = paginator.get_page(page_number)  # Obtenha as imagens para a página atual

    template = loader.get_template("listaImagens/index.html")
    context = {
        "imagens": imagens,
    }
    return HttpResponse(template.render(context, request))    


    