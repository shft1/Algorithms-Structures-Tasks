import sys


def main():
    n = int(sys.stdin.readline())

    limit = n + 1
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    if is_prime[n]:
        print(1)
        print(n)
        return

    def find_two_primes(s):
        for p in range(2, s):
            if is_prime[p] and is_prime[s - p]:
                return p, s - p
        return None

    if n % 2 == 0:
        a, b = find_two_primes(n)
        print(2)
        print(a, b)
    else:
        if is_prime[n - 2]:
            print(2)
            print(2, n - 2)
        else:
            a, b = find_two_primes(n - 3)
            print(3)
            print(3, a, b)


if __name__ == "__main__":
    main()
