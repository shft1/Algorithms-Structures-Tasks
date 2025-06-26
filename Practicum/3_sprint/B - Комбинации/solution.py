import sys


def permutation(str_nums, max_deep, cur_deep=0, perm=[]):
    if cur_deep == max_deep:
        sys.stdout.write("".join(perm) + " ")
        return
    for str in str_nums[cur_deep]:
        perm.append(str)
        permutation(str_nums, max_deep, cur_deep + 1, perm)
        perm.pop()


def solution():
    info = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    strs_nums = [info[num] for num in sys.stdin.readline().rstrip()]

    permutation(strs_nums, len(strs_nums))


if __name__ == "__main__":
    solution()
