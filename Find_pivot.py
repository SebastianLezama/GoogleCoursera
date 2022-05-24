
shifted_array1 = [13, -2, 3, 4, 7, 8, 9, 11]
shifted_array2 = [11, 13, -2, 3, 4, 7, 8, 9]
shifted_array3 = [9, 11, 13, -2, 3, 4, 7, 8]
shifted_array4 = [8, 9, 11, 13, -2, 3, 4, 7]
shifted_array5 = [7, 8, 9, 11, 13, -2, 3, 4]
shifted_array6 = [4, 7, 8, 9, 11, 13, -2, 3]
shifted_array7 = [3, 4, 7, 8, 9, 11, 13, -2]
#                L           M           R



def find_pivot(list):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if list[mid] < list[mid - 1]:
            return mid
        if list[mid] > list[mid + 1]:
            return mid + 1
            

        if list[right] < list[left] > list[mid]:
            print('A')
            right = mid - 1
            if list[right] > list[mid]:
                print('a')
                return mid  
        else:
            if list[left] > list[right] < list[mid]:
                print('B')
                left = mid + 1
                if list[left] < list[mid]:
                    print('b')
                    return mid
    return 'Fail'



if __name__ == '__main__':
    print(find_pivot(shifted_array2))
        

