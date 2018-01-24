def fibonacci(n):
    """ Recursive solution to return a fibonacci sequence """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """ Recursive solution to return a lucas sequence """
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0, y=1):
    if x==2 and y==1:
        return lucas(n)
    else:
        return fibonacci(n)

print("Start")
if __name__ == "__main__":
    print(fibonacci(4))
    print(lucas(4))
    print(sum_series(4))
    print(sum_series(4, 2, 1))
