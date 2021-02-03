real = 'BRL'
dollar = 'USD'
euro = 'EUR'


def conversion(amout, from_to, to, rate):
    if from_to == real and to == dollar:
        return real_dollar(amout, rate)
    elif from_to == dollar and to == real:
        return dollar_real(amout, rate)
    elif from_to == real and to == euro:
        return real_euro(amout, rate)
    elif from_to == euro and to == real:
        return euro_real(amout, rate)


def real_dollar(amout, rate):
    return {"valorConvertido": amout/rate, "simboloMoeda": '$'}


def dollar_real(amout, rate):
    return {"valorConvertido": amout*rate, "simboloMoeda": 'R$'}


def real_euro(amout, rate):
    return {"valorConvertido": amout/rate, "simboloMoeda": '€'}


def euro_real(amout, rate):
    return {"valorConvertido": amout*rate, "simboloMoeda": 'R$'}
