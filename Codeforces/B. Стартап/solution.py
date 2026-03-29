import sys


def main() -> None:
    s = sys.stdin.read().strip()
    if not s:
        return

    digits_sum = sum(ord(ch) - ord("0") for ch in s)
    current = int(s)
    best_answer = None
    best_key = None

    for digit in range(0, 10, 2):
        if (digits_sum - (ord(s[-1]) - ord("0")) + digit) % 3 != 0:
            continue

        candidate = s[:-1] + str(digit)
        if len(candidate) > 1 and candidate[0] == "0":
            continue

        candidate_value = int(candidate)
        changes = 0 if candidate == s else 1
        key = (changes, abs(candidate_value - current), candidate_value)

        if best_key is None or key < best_key:
            best_key = key
            best_answer = candidate

    sys.stdout.write(best_answer)


if __name__ == "__main__":
    main()
