"""
SELECTION SORT

Basicamente quando o array é percorrido é buscado o menor elemento e quando
este for encontrado é substituído pelo atual.

Referências:
  - https://pt.wikipedia.org/wiki/Selection_sort
  - https://visualgo.net/bn/sorting
"""

def selection_sort(items_list):
    for index in range(0, len(items_list)):
        min_index = index
        for right in range(index + 1, len(items_list)):
            if items_list[right] < items_list[min_index]:
                min_index = right
        items_list[index], items_list[min_index] = items_list[min_index], items_list[index]
    return items_list


items_list = [9, 8, 7, 3, 4, 2, 1]
print(selection_sort(items_list))

