import sys

# def solution(s, seq):
#     src_len = len(s)
#     updt_str = s
#     for t, k in seq:
#         size_t = len(t)
#         size_old_str = len(updt_str)
#         updt_str.extend([" "] * size_t)
#         ins_idx = int(k) + (size_old_str - src_len)
#         for i in range(size_old_str - 1, ins_idx - 1, -1):
#             updt_str[i + size_t] = updt_str[i]
#         for i in range(size_t):
#             updt_str[ins_idx + i] = t[i]
#     return "".join(updt_str)


def solution(s, n):
    parts = {}
    for _ in range(n):
        t, k = sys.stdin.readline().rstrip().split()
        parts[int(k)] = t
    for i in range(len(s)):
        if i in parts:
            sys.stdout.write(parts[i])
        sys.stdout.write(s[i])
    if len(s) in parts:
        sys.stdout.write(parts[len(s)])


def main():
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    solution(s, n)


if __name__ == "__main__":
    main()
