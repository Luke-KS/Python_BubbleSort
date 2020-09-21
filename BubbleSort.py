unsorted = [3, 1, 2, 4, 9, 10, 8, 7, 5, 6, 100, 99, 88, 321, 3, 364, 2, 0, 1]


def bubbleSort(list):
    change = True
    while change:
        change = False
        for x in range(len(list) - 1):
            if list[x] > list[x + 1]:
                list[x], list[x + 1] = list[x + 1], list[x]
                change = True
    return list


print(bubbleSort(unsorted))
