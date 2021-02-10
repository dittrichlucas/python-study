from requests import get
REAL = 'BRL'
DOLLAR = 'USD'
EURO = 'EUR'


def conversion(amout, from_to, to, rate):
    if from_to == REAL and to == DOLLAR:
        return real_dollar(amout, rate)
    elif from_to == DOLLAR and to == REAL:
        return dollar_real(amout, rate)
    elif from_to == REAL and to == EURO:
        return real_euro(amout, rate)
    elif from_to == EURO and to == REAL:
        return euro_real(amout, rate)


def real_dollar(amout, rate):
    return {"valorConvertido": amout/rate, "simboloMoeda": '$'}


def dollar_real(amout, rate):
    return {"valorConvertido": amout*rate, "simboloMoeda": 'R$'}


def real_euro(amout, rate):
    return {"valorConvertido": amout/rate, "simboloMoeda": '€'}


def euro_real(amout, rate):
    return {"valorConvertido": amout*rate, "simboloMoeda": 'R$'}


def get_exchange():
    req = get('https://api.exchangeratesapi.io/latest?base=BRL')
    data = req.json()

    return data
