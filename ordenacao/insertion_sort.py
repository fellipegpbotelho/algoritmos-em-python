"""
INSERTION SORT

Basicamente quando o array é percorrido é verificado se o item da esquerda é
menor, se for é feita a troca até que o elemento fique na sua posição correta.

Referências:
  - https://pt.wikipedia.org/wiki/Insertion_sort
  - https://visualgo.net/bn/sorting
"""


def sort(array):
    for p in range(0, len(array)):
        current_element = array[p]
        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1
        array[p] = current_element
    return array


array = [9, 7, 8, 1, 3, 5, 2, 0]
copy_array = array[:]

print(sort(array))
