from django.http import HttpResponse
from django.template import loader

from CoviDATA_app.models import illustrate
from CoviDATA_app.models import estate

def index(request):
    template = loader.get_template('index.html')
    context = { ## Relacionado com o banco de dados que sera usado para o template em questao
        'logo': illustrate.objects.get(name='logo'),
        'brasil': illustrate.objects.get(name='brasil'),
        'covid_1': illustrate.objects.get(name="covid_1"),
        'covid_2': illustrate.objects.get(name="covid_2"),
        'covid_3': illustrate.objects.get(name="covid_3"),
        'lateral': illustrate.objects.get(name="lateral"),
    }
    return HttpResponse(template.render(context, request))

def numcasos(request):
    template = loader.get_template('numcasos.html')
    context = { ## Relacionado com o banco de dados que sera usado para o template em questao
        'logo': illustrate.objects.get(name='logo'),
        'estates': estate.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def analicasos(request):
    template = loader.get_template('analicasos.html')
    context = { ## Relacionado com o banco de dados que sera usado para o template em questao
        'logo': illustrate.objects.get(name='logo'),
        'estates': estate.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def controlgastos(request):
    template = loader.get_template('controlgastos.html')
    context = { ## Relacionado com o banco de dados que sera usado para o template em questao
        'logo': illustrate.objects.get(name='logo'),
        'estates': estate.objects.all(),
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
