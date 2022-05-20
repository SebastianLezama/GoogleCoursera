nums = [2, 3, 4, 5, 6]

def tree_sum(nums):
    total = 0
    for i in nums:
        total += i
    return total

if __name__ == '__main__':
    print(tree_sum(nums))