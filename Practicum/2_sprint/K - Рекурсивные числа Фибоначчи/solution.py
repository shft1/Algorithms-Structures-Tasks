import sys

# Данная функция работает за O(2^n)
# def fibonacci(n):
#     if n <= 1:
#         return 1
#     return fibonacci(n - 2) + fibonacci(n - 1)


def fibonacci(n):
    if n <= 1:
        return None, 1
    if n == 2:
        return 1, 2
    n_2, n_1 = fibonacci(n - 1)
    return n_1, n_2 + n_1


def solution():
    n = int(sys.stdin.readline().rstrip())
    _, res = fibonacci(n)
    return res


if __name__ == "__main__":
    sys.stdout.write(str(solution()))
