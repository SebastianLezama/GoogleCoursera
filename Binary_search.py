# binary search that returns index of the target number in the sorted array.
# if not it should return -1.

array = [-2, 3, 4, 7, 8, 9, 11, 13]
target = 9


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


if __name__ == '__main__':
    print(search(array, target))

# solve a shifted binary search

shifted_array = [8, 9, 11, 13, -2, 3, 4, 7]


