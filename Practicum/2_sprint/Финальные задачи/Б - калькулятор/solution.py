import sys


def solution():
    stack = []
    for var in sys.stdin.readline().rstrip().split():
        if var in ["+", "-", "*", "/"]:
            summit, pre_summit = stack.pop(), stack.pop()
            if var == "+":
                stack.append(pre_summit + summit)
            elif var == "-":
                stack.append(pre_summit - summit)
            elif var == "*":
                stack.append(pre_summit * summit)
            else:
                stack.append(pre_summit // summit)
        else:
            stack.append(int(var))
    return stack[-1]


if __name__ == "__main__":
    sys.stdout.write(f"{solution()}\n")
