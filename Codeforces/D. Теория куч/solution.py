import sys


def final_difference(diff: int, x: int, q: int) -> int:
    if q == 0:
        return diff

    step = 2 * x

    if diff >= 0:
        straight = diff // step
        if q <= straight:
            return diff - step * q

        current = diff - step * straight
        remaining = q - straight
        return current if remaining % 2 == 0 else current - step

    straight = (-diff) // step
    if q <= straight:
        return diff + step * q

    current = diff + step * straight
    remaining = q - straight

    if current == 0:
        return 0 if remaining % 2 == 0 else -step

    return current if remaining % 2 == 0 else current + step


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 4:
        return

    n, m, x, q = data[:4]
    total = n + m
    diff = final_difference(n - m, x, q)

    first = (total + diff) // 2
    second = total - first
    sys.stdout.write(f"{first} {second}")


if __name__ == "__main__":
    main()
