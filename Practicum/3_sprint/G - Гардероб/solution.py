import sys


def solution():
    n = sys.stdin.readline().rstrip()
    nums = list(map(int, sys.stdin.readline().rstrip().split()))

    main_idx = 0
    count_arr = [0] * 3

    for num in nums:
        count_arr[num] += 1

    for value in range(3):
        for _ in range(count_arr[value]):
            nums[main_idx] = value
            main_idx += 1

    return " ".join(map(str, nums))


if __name__ == "__main__":
    sys.stdout.write(solution())
