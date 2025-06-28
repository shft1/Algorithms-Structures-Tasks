# import sys
# from functools import cmp_to_key


# def less(num1, num2):
#     if num1 == num2:
#         return -1
#     min_num = min(num1, num2)
#     max_num = max(num1, num2)
#     len_min = len(min_num)
#     for i in range(len_min):
#         if int(min_num[i]) > int(max_num[i]):
#             if num1 == min_num:
#                 return -1
#             return 1
#         if int(min_num[i]) < int(max_num[i]):
#             if num1 == min_num:
#                 return 1
#             return -1
#     if max_num[len_min] > min_num[0]:
#         if max_num == num1:
#             return -1
#         return 1
#     if max_num[len_min] < min_num[0]:
#         if max_num == num1:
#             return 1
#         return -1
#     else:
#         return 1


# def solution():
#     n = sys.stdin.readline().rstrip()
#     numbers = sys.stdin.readline().rstrip().split()
#     sys.stdout.write("".join(sorted(numbers, key=cmp_to_key(less))))


# if __name__ == "__main__":
#     solution()


import sys
from functools import cmp_to_key


def comrporator(x, y):
    if x + y > y + x:
        return -1
    return 1


def solution():
    n = sys.stdin.readline().rstrip()
    numbers = sys.stdin.readline().rstrip().split()
    sys.stdout.write("".join(sorted(numbers, key=cmp_to_key(comrporator))))


if __name__ == "__main__":
    solution()
