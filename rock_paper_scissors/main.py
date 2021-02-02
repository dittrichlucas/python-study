""" Number Guessing
----------------------------
This program or a mini-game is designed when you don’t have anyone to play or you
are under lockdown alone. There are a number of functions that this program
requires so let us have an overview of each.

- a random function: to generate rock, paper, or scissors.
- valid function: to check the validity of the move.
- result function: to declare the winner of the round.
- scorekeeper: to keep track of the score.

The program requires the user to make the first move before it makes one the move.
Once the move is validated the input is evaluated, the input entered could be a
string or an alphabet. After evaluating the input string a winner is decided by
the result function and the score of the round is updated by the scorekeeper function.
----------------------------
"""
import random


# TODO: adicionar validações (mapear cenários)
# TODO: tornar a dinâmica do jogo mais amigável
# TODO: adicionar testes

choices = 'RPS'
my_score = 0
computer_score = 0


def random_choice() -> str:
    return random.choice(choices)


def valid_move(input: str) -> bool:
    return True if input and input.upper() in choices else False


def scorekeeper(winner) -> None:
    global computer_score, my_score
    if winner == 'me':
        print('You win!')
        my_score += 1
    elif winner == 'computer':
        print('You lose!')
        computer_score += 1
    elif winner == 'empate':
        print('A tie!')


def game() -> None:
    winner = ''

    try:
        my_choice = input(
            'Type your choice [ R(rock) P(paper) S(scissors) ]: ').upper()

        move = valid_move(my_choice)

        if move:
            computer_choice = random_choice()
            if computer_choice == 'R':
                if my_choice == 'S':
                    winner = 'computer'
                elif my_choice == 'R':
                    winner = 'empate'
                elif my_choice == 'P':
                    winner = 'me'
            elif computer_choice == 'P':
                if my_choice == 'S':
                    winner = 'me'
                elif my_choice == 'R':
                    winner = 'computer'
                elif my_choice == 'P':
                    winner = 'empate'
            elif computer_choice == 'S':
                if my_choice == 'S':
                    winner = 'empate'
                elif my_choice == 'R':
                    winner = 'me'
                elif my_choice == 'P':
                    winner = 'computer'

        if not move:
            game()

        scorekeeper(winner)

        again = input('You play again? (y/n): ')
        if again:
            if again.lower() == 'y':
                game()
            elif again.lower() == 'n':
                print('\n------------------------------')
                print('| SCORE                      |')
                print('------------------------------')
                print(
                    f'| You: {my_score}        Computer: {computer_score}  |')
                print('------------------------------')
                print('\nBye\n')
                exit()
        else:
            print('no choice')

    except KeyboardInterrupt:
        pass


game()
