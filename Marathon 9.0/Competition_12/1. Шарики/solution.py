import sys


def main():
    balls = list(map(int, sys.stdin.readline().rstrip().split()))

    runs = []
    for ball in balls:
        if runs and runs[-1][0] == ball:
            runs[-1][1] += 1
        else:
            runs.append([ball, 1])

    stack = []
    destroyed = 0

    for color, count in runs:
        if stack and stack[-1][0] == color:
            stack[-1][1] += count
        else:
            stack.append([color, count])

        if stack[-1][1] >= 3:
            destroyed += stack[-1][1]
            stack.pop()

    print(destroyed)


if __name__ == "__main__":
    main()
