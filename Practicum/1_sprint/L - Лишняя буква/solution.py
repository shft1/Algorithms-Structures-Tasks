import sys


def solution():
    num = int(sys.stdin.readline().rstrip())
    is_prime = False
    even_nums = []

    while not is_prime:
        i = 2
        while i**2 <= num:
            if num % i == 0:
                even_nums.append(i)
                num //= i
                break
            i += 1

        if i**2 > num:
            is_prime = True
            even_nums.append(num)

    even_nums.sort()
    print(*even_nums)


if __name__ == "__main__":
    solution()
