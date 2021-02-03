from fastapi import FastAPI
from conversion import conversion  # type: ignore

app = FastAPI()

"""
PADRÃO DA ROTA:
http://localhost:8000/exchange/{amount}/{from}/{to}/{rate}
http://localhost:8000/exchange/10/BRL/USD/4.50

TODO: gerar modelo para não passar muitos parâmetros
TODO: desenvolver testes
TODO: consumir dados de uma api pública para apresentar dados em tempo real
"""


@app.get('/exchange/{amount}/{from_to}/{to}/{rate}')
async def root(amount: float, from_to: str, to: str, rate: float):
    return conversion(amount, from_to, to, rate)
