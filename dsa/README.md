~~Inicialmente vou escrever aqui o que eu estou aprendendo sobre estruturas de dados e algoritmos.~~

## Por quê?

Como eu estou migrando minha carreira para dev, estou sentindo muita falta de entender como as coisas funcionam para poder escrever códigos claros, elegantes, funcionais e otimizados.

A partir disso, percebi que sei quase nada sobre estruturas de dados e algoritmos, suas aplicações e operações.

Assim, resolvi focar em estudar isso e praticar por meio de desafios encontrados nas mais variadas plataformas de _challenges_.

## Arrays

- Nada mais são do que listas de coisas.
- Normalmente são identificadas pelo símbolo **`[]`**.

### Operações

- `append`: vai adicionar um elemento no final da lista
- `insert`: precisa passar o índice e o elemento
- `pop`: vai remover um elemento com base no índice passado (caso nenhum seja passado, vai remover o último)
- `remove`: vai remover a primeira ocorrência do elemento passado
- `index`: vai retornar o primeiro índice para o elemento passado
- `reverse`: inverte a lista

- `merge`
- `sort`
- `search/find`
- `replace`

## Linked list

Uma lista encadeada é um array em que os elementos apontam para si, ou seja, cada elemento tem o 'endereço' do próximo/anterior.

Assim, elas podem ser de 2 tipos:

1. singular/simples: onde os elementos possuem apenas o endereço do próximo
2. dupla: onde os elementos possuem o endereço do elemento anterior e o do próximo

https://aprendacompy.readthedocs.io/pt/latest/capitulo_17.html
https://carboncoffee.hashnode.dev/linked-list-using-python

### Algoritmos de busca

#### Linear search

Esse é um dos algoritmos mais simples, visto que, para um dado array de tamanho n, caso eu queria encontrar o elemento x, basta iterar o array até encontrar o elemento.

Para ilustrar:

```python
def linear_search(array, x):
    for i in array:
        if i == x:
            return 'found'

    return 'not found'

linear_search([1, 2, 3], 1) # 'found'
```

### Binary search

Diferente da busca linear, para a busca binária, é necessário que o array esteja ordenado (sorted).

https://klauslaube.com.br/2019/05/10/algoritmos-de-ordenacao-parte-1.html
https://carboncoffee.hashnode.dev/datastructures

https://www.hebergementwebs.com/news/learning-roadmap-for-data-structures-and-algorithms

https://www.programiz.com/dsa

Challenges:
https://binarysearch.com/problems?difficulty=0&tag=array
https://www.techiedelight.com/list-of-problems/
https://www.hackerearth.com/practice/data-structures/arrays/1-d/tutorial/
https://www.hackerrank.com/domains/data-structures?filters%5Bsubdomains%5D%5B%5D=arrays
https://app.codility.com/programmers/lessons/1-iterations/

