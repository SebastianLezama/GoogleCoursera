# binary search that returns index of the target number in the sorted array.
# if not it should return -1.

array = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 3


def search(list, number):
    left = 0
    right = len(list) - 1
    while left < right:
        middle = int((left + right) / 2)
        if list[middle] == number:
            return middle
        elif number < list[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


# solve a shifted binary search

shifted_array = [8, 9, 11, 13, -2, 3, 4, 7]


def shifted_search(list, number):
    left = 0
    right = len(list) - 1
    while list[left] < list[right]:
        return search(list, number)
    while list[left] > list[right]:
        middle = int((left + right) / 2)
        if list[middle] == number:
            return middle
        elif list[middle] > list[right]:
            left = middle + 1
            if list[left] < list[middle]:
                new_list = list[left : len(list)] + list [0 : left]
                return search(new_list, number) + left
        



if __name__ == '__main__':
    print(shifted_search(shifted_array, target))