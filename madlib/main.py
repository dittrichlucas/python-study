"""Mad Libs Generator
----------------------------
This python beginner project is a good start for beginner software developers
as it has concepts like strings, variables, and concatenation.
Mad Libs Generator teaches to manipulate user-inputted data as the Mad Libs refer
to a series of inputs that a user enters. The input from the user could be anything
from an adjective, a pronoun, or even a verb. After all the inputs are entered the
application takes all the data and arranges it to build a story template.
----------------------------
"""

import random

# TODO: criar uma função para gerar as frases OK
# TODO: adicionar validações (mapear possíveis cenários) OK
# TODO: tornar o loop mais dinâmico, ou seja, o usuário que controla quantas vezes pretende gerar as frases OK
# TODO: ter mais de uma frase para preencher OK
# TODO: gerar um random para as frases OK
# TODO: após finalizadas as devidas validações, implementar testes unitários
# TODO: tornar as frases mais amigáveis (cor, negrito, espaço...)


def generate_madlib():
    madlib = random_madlib()
    again = 'y'
    try:
        while again == 'y':
            noun = input('Enter a noun: ')
            adjective = input('Enter an adjective: ')

            print(madlib.format(adjective, noun))

            again = input('Again? (y/n): ')
            if again:
                if again.lower() == 'y':
                    generate_madlib()
                elif again.lower() == 'n':
                    print('Bye')
                    exit
                else:
                    print('no choice')
            else:
                print('no choice')
    except (KeyboardInterrupt):
        exit


def random_madlib():
    first = 'Today I went to the zoo. I saw a(n) {} {} jumping up and down in its tree.\n'
    # se for essa o substantivo vem primeiro
    second = """I wore a blue and white striped, long sleeve {} with a collar on
    it, a red tie, dark gray pants, white socks, black shoes, and a(n) {} hat."""
    third = ' I gaze at his {} {}'
    madlibs = (first, second, third)

    return random.choice(madlibs)


generate_madlib()
