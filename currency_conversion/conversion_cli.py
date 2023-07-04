"""
como esse cara vai ser mais prático, visto que vou consumir direto da API,
preciso apenas escolher qual é a moeda base e pra qual moeda quero converter
"""
from typing import Dict
from requests import get

BASE_URL = 'https://api.exchangeratesapi.io/latest'


def get_data(base: str) -> Dict:
    req = get(f'{BASE_URL}?base={base}')

    return req.json()


def get_currency():
    req = get(f'{BASE_URL}')
    data = req.json()

    return data['rates'].keys() if data.keys() else ''


def conversion():
    base = input('Selecione a moeda base (BRL / EUR / USD): ')
    value = int(input('Informe o valor que você deseja converter: '))
    convert = input('Seleciona a moeda para qual você quer converter: ')
    data = get_data(base)
    res = value * data['rates'][convert]
    # currency = get_currency()
    print(f'O resultado é: {round(res, 2)}')
    # base = input('Selecione a moeda base:')


conversion()
# test = get_data('')
# print(test)
