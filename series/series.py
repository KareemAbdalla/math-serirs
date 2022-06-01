
def fibonacci(n):  # 0, 1, 1, 2, 3, 5, 8, 13

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):  # 2, 1, 3, 4, 7, 11, 18, 29

    if n == 0:
        return 2
    if n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, idx0=0, idx1=1):  # 2, 1, 3, 4, 7, 11, 18, 29

    if n == 0:
        return idx0
    if n == 1:
        return idx1

    return sum_series(n - 1, idx0, idx1) + sum_series(n - 2, idx0, idx1)


if __name__ == "__main__":
    print(fibonacci(7))
    print(lucas(7))
    print(sum_series(7))
    print(sum_series(7, 5, 2))
    print(sum_series(7, 2, 1))

