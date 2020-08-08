from django.core.management.base import BaseCommand, CommandError
from CoviDATA_app.models import estate

import csv

class Command(BaseCommand): 
  
    help = 'atualiza o banco de dados baixado do site do governo'

    def handle(self, *args, **kwargs):
        file = open('covid_data.csv')
        ler = csv.reader(file)
        for linha in ler:
            estado,sigla,data,semanaEpi,populacaoTCU2019,casosAcumulado,casosNovos,obitosAcumulado,obitosNovos,RecuperadosNovos,MMNCasos,MMNObitos = linha
            if estado == 'estado':
                continue
            if MMNCasos in [None, '']:
                MMNCasos = 0.0
            if MMNObitos in [None, '']:
                MMNObitos = 0.0
            if RecuperadosNovos in [None, '']:
                RecuperadosNovos = '0.0'
            atual, created = estate.objects.get_or_create(
                name = estado
            )
            atual.casos = int(casosAcumulado)
            atual.obitos = int(obitosAcumulado)
            atual.media_movel_casos = float(MMNCasos)
            atual.media_movel_obitos = float(MMNObitos)
            atual.recuperados = int(RecuperadosNovos[:-2])
            atual.save()
