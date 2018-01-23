def fibonacci(n):
    """ Recursive solution to return a fibonacci sequence """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print("Start")
if __name__ == "__main__":
    print(fibonacci(3))

# for number in range(0,10):
#     print (fibonacci(number), end = ' ')

