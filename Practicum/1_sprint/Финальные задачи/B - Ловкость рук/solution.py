import sys


def solution():
    k2 = int(sys.stdin.readline().rstrip()) * 2
    cout_numb = [0] * 10
    ball = 0
    for _ in range(4):
        for char in sys.stdin.readline().rstrip():
            if char != '.':
                 cout_numb[int(char)] += 1
    for t in range(1, 10):
        if cout_numb[t] != 0 and k2 >= cout_numb[t]:
            ball += 1
    return str(ball)

if __name__ == "__main__":
    sys.stdout.write(solution())