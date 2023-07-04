"""
Dado um array de tamanho ímpar n, encontre o único elemento não pareado

A = [1, 2, 3, 1, 2]
return 3
"""

a = [1, 2, 3, 1, 2, 2, 2]
for i in range(len(a)):  # usa o índice
    print(i)
    next_index = i+1 if len(a)-1 >= i+1 else i
    print(next_index)
    print(a.index(a[i], a[next_index], a[len(a)-1]))
    print(a.index(a[i]))

# print(tmp)
