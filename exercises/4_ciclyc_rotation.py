"""
Eu vou receber um array e um número.

A partir deles, preciso rotacionar o array a quantidade de vezes do número passado.

A rotação do array consiste em o último número ser o primeiro e os demais moverem-se para a direita.
"""

array = []
k = 3

for i in range(k):
    if array:
        last_element = array[len(array)-1]
        array.pop(len(array)-1)
        array.insert(0, last_element)

print(array)
