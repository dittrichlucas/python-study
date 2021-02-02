""" Number Guessing
----------------------------
This project is an exciting fun game for beginners to build up.
The program generates a random number from 1 to 10, or 1 to 100 any range that is
specified and the user must guess the number after a hint from the computer.
Every time a user’s guess is wrong they are prompted with more hints to make it
easier for them to guess the number but at the cost of reducing the score.
The clue any math clue like multiples, divisible, greater or smaller, or a combination of all.

The program also requires functions to check if an actual number is entered by
the user or not, to compare the input number with the actual number, to find
the difference between the two numbers.
----------------------------
"""
import random
from time import sleep
from colors import bcolors  # type: ignore


# TODO: tornar loop em uma função OK
# TODO: tornar o jogo mais amigável
# TODO: transformar as mensagens dos prints em constantes
# TODO: melhorar as mensagens de erro (mapear cenários)
# TODO: criar readme e arquivos necessários para subir no github
# TODO: adicionar testes
print('\nStart Game...')
sleep(0.8)

score = 0
attempts = 0
color_score = bcolors.OKGREEN + bcolors.BOLD
color_input = bcolors.OKBLUE + bcolors.BOLD
color_tips = bcolors.OKCYAN + 'Dica:'


def random_number() -> str:
    return str(random.randrange(1, 10))


def show_score(attempts) -> None:
    global score
    if attempts == 1:
        score += 10
    elif attempts == 2:
        score += 5
    elif attempts == 3:
        score += 3
    elif attempts >= 4:
        score += 1


def game() -> None:
    global attempts

    choice = random_number()
    again = True

    try:
        while again:
            my_choice = input(
                color_input + '\nType what do you think was my choice: ')

            if(choice != my_choice):
                attempts += 1
                again = True

                if choice > my_choice:
                    print(bcolors.BOLD + 'Dica: o número é maior')
                elif choice < my_choice:
                    print(color_tips + 'o número é menor')

            elif(choice == my_choice):
                attempts += 1

                show_score(attempts)

                again_to = input(color_input + '\nAgain? (y/n): ')

                if(again_to == 'y'):
                    choice = random_number()
                    attempts = 0
                    again = True
                elif(again_to == 'n'):
                    again = False

                    print(color_score + '\nYour score is: {}\n'.format(score))

    except KeyboardInterrupt:
        pass


game()
