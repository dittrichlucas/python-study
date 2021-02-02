import csv


# TODO: melhorar apresentação das perguntas
# TODO: adicionar validações (mapear cenários)
# TODO: adicionar testes
OKGREEN = '\033[92m'
OKBLUE = '\033[94m'


def quiz():
    score = 0

    try:
        with open('problems.csv', 'r') as file:
            problems = csv.reader(file)

            for col in problems:
                answer = input(OKBLUE +
                               f'{problems.line_num}. {col[0]} = ')

                if answer is not None:
                    if answer == col[1]:
                        score += 1
                elif answer is None:
                    exit

        print(OKGREEN + f'\nYour score: {score}\n')

    except KeyboardInterrupt:
        pass


quiz()
