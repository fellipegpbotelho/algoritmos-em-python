"""
BUBBLE SORT

A ideia do bubble sort é percorrer o array diversas vezes, e a cada passagem
fazer flutuar para o topo o maior elemento da sequência.

Quando a lista está quase sorteada, ou seja não é requerido que sejam
realizadas muitas trocas o bubble_sort funciona muito bem, do contrário
a performance não é tão satisfatória.

Referências:
  - https://pt.wikipedia.org/wiki/Bubble_sort
  - https://visualgo.net/bn/sorting
"""


def sort(array):
    for final in range(len(array), 0, -1):
        exchanging = False
        for c in range(0, final - 1):
            if array[c] > array[c + 1]:
                array[c], array[c + 1] = array[c + 1], array[c]
                exchanging = True
            if not exchanging:
                break
    return array


default_list = [8, 7, 5, 3, 1, 2, 9, 6, 4]
sorted_list = sorted(default_list)

print(sort(default_list))
