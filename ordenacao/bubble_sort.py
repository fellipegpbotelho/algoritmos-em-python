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

def sort(items_list):
    for final in range(len(items_list), 0, -1):
        exchanging = False
        for current in range(0, final - 1):
            if items_list[current] > items_list[current + 1]:
                items_list[current], items_list[current + 1] = items_list[current + 1], items_list[current]
                exchanging = True
            if not exchanging:
                break
    return items_list


default_list = [8, 7, 5, 3, 1, 2, 9, 6, 4]
sorted_list = sorted(default_list)

print(sort(default_list))
