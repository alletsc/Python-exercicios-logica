import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando csv')
        dados = entrada.read().decode('latin1')
        print('Download Completo')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]}: {cidade[3]}')  # nona coluna e quarta coluna


read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
