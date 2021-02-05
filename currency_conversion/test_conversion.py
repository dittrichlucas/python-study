from conversion import conversion


def test_real_dollar():
    amout = 10
    from_to = 'BRL'
    to = 'USD'
    rate = 4.5
    got = conversion(amout, from_to, to, rate)

    assert got == {"valorConvertido": amout/rate, "simboloMoeda": '$'}


def test_dollar_real():
    amout = 10
    from_to = 'USD'
    to = 'BRL'
    rate = 4.5
    got = conversion(amout, from_to, to, rate)

    assert got == {"valorConvertido": amout*rate, "simboloMoeda": 'R$'}


def test_real_euro():
    amout = 10
    from_to = 'BRL'
    to = 'EUR'
    rate = 4.5
    got = conversion(amout, from_to, to, rate)

    assert got == {"valorConvertido": amout/rate, "simboloMoeda": '€'}


def test_euro_real():
    amout = 10
    from_to = 'EUR'
    to = 'BRL'
    rate = 4.5
    got = conversion(amout, from_to, to, rate)

    assert got == {"valorConvertido": amout*rate, "simboloMoeda": 'R$'}
