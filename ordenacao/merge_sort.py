"""
MERGE SORT

Sua ideia básica consiste em dividir (o problema em vários subproblemas e resolver esses subproblemas através da recursividade) e conquistar (após todos os subproblemas terem sido resolvidos ocorre a conquista que é a união das resoluções dos subproblemas).

Referências:
  - https://pt.wikipedia.org/wiki/Merge_sort
  - https://visualgo.net/bn/sorting
"""


def sort(array):
    return sort_half(array, 0, len(array) - 1)


def sort_half(array, start, end):
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, start, middle)
    sort_half(array, middle + 1, end)

    return merge(array, start, end)


def merge(array, start, end):
    array = array[start:end + 1] = sorted(array[start:end + 1])
    return array


array = [9, 7, 8, 1, 3, 5, 2, 0]

print(sort(array))
