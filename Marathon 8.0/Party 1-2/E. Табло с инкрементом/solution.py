import sys


def solution(n, k):
    if n % 10 == 0:
        return n
    if n % 10 == 5:
        if k >= 1:
            return n + 5
        return n

    steps = [n]
    for _ in range(4):
        steps.append(steps[-1] + (steps[-1] % 10))
    if k <= 4:
        return steps[k]

    base = [steps[-1]]
    for _ in range(3):
        base.append(base[-1] + (base[-1] % 10))
    k -= 4
    curr_base = base[k % 4]
    ten, unit = curr_base // 10, curr_base % 10
    full_cicle = k // 4 * 20
    return ten * 10 + full_cicle + unit


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(solution(n, k)))


if __name__ == "__main__":
    main()
