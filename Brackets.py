# queues problem: true if brackets are balanced

array = ("([])(){{}(())(){}}{")

shifted_array = [8, 9, 11, 13, -2, 3, 4, 7]

list = shifted_array[3:] + shifted_array[: 3]
print(list)
print(len(list)-1)