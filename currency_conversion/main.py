from fastapi import FastAPI
from conversion import conversion, get_exchange  # type: ignore

app = FastAPI()

"""
PADRÃO DA ROTA:
http://localhost:8000/exchange/{amount}/{from}/{to}/{rate}
http://localhost:8000/exchange/10/BRL/USD/4.50

TODO: consumir dados de uma api pública para apresentar dados em tempo real (ok)
TODO: usar graphql
TODO: mudar de path params para body
"""


@app.get('/exchange/{amount}/{from_to}/{to}/{rate}')
async def root(amount: float, from_to: str, to: str, rate: float):
    return conversion(amount, from_to, to, rate)


@app.get('/exchange')
async def actual_rate():
    return get_exchange()
