import sys


def main():
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
    sums = {0}
    for num in nums:
        curr = set()
        for sum in sums:
            curr.add(sum + num)
        sums.update(curr)
    diff = 101
    res = -1
    for sum in sums:
        curr_diff = abs(100 - sum)
        if curr_diff == 0:
            diff = curr_diff
            res = sum
        elif curr_diff < diff:
            diff = curr_diff
            res = sum
        elif curr_diff == diff and sum > res:
            res = sum
            diff = curr_diff
    sys.stdout.write(str(res))


if __name__ == '__main__':
    main()
