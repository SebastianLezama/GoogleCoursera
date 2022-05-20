from datetime import datetime
start = datetime.now()
# Fibonnacci sequence, enter sequence number to caculate
def fib(n):
    try:
        if 0 < n == 1:
            return n
        elif n == 2:
            return n - 1
        elif n > 2:
            return fib(n - 1) + fib(n - 2)
        else:
            print("No negative numbers please.")
    except:
        print("No negative numbers please.")
    

if __name__ == '__main__':
    print('The result is: ' + str(fib(int(input('Enter Fibonnacci sequence number: ')))))
    print(datetime.now()-start)

# n * (n+(n-1))
# 1, 1, 2, 3, 5, 8