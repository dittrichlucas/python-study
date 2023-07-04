"""
Um gap binário é uma sequência de 0s em um valor binário, por exemplo:
1001 - o gap é 2
10001001 - temos 2 gaps: 3 e 2
100 - não há gap

Assim, o desafio proposto é encontrar o maior gap dentro de um número
"""


def solution(N):
    n_str = str(bin(N))
    count = 0
    new_count = []
    for i in n_str[2:]:
        if i == '1':
            new_count.append(count)
            count = 0
            continue

        count += 1

    return max(new_count) if new_count else 0
