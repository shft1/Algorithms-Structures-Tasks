import sys


def main():
    s = sys.stdin.readline().strip()

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    openings = set(pairs.values())

    def is_correct(sequence: str) -> bool:
        stack = []

        for char in sequence:
            if char in openings:
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return not stack

    n = len(s)
    if n == 0:
        print("YES")
        return

    if n % 2 == 1:
        print("NO")
        return

    for shift in range(n):
        rotated = s[shift:] + s[:shift]
        if is_correct(rotated):
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    main()
