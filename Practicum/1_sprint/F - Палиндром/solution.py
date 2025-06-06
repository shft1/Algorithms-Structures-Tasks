import sys


def solution():
    p = sys.stdin.readline().rstrip()
    l, r = 0, len(p) - 1

    while l < r:
        if not p[l].isalnum():
            l += 1
            continue
        if not p[r].isalnum():
            r -= 1
            continue
        if p[l].lower() != p[r].lower():
            return False
        l += 1
        r -= 1

    return True

if __name__ == "__main__":
    sys.stdout.write(str(solution()))