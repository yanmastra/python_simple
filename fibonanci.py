def do_fibo():
    length = int(input("Length of fibonacci ?:"))
    result = []
    for i in range(length):
        result.append(fibo(i))
    print(result)


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


if __name__ == '__main__':
    continue_ = 1
    while continue_ == 1:
        do_fibo()
        continue_ = int(input("Repeat ? 1/0:"))

