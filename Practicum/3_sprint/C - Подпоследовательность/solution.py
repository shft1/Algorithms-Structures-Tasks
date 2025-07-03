import sys


def solution():
    """
    T: O(t)
    M: O(1)
    """

    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    s_len, t_len = len(s), len(t)

    s_idx, t_idx = 0, 0
    while s_idx != s_len and t_idx != t_len:
        if t[t_idx] == s[s_idx]:
            s_idx += 1
        t_idx += 1

    return str(s_idx == s_len) + "\n"


if __name__ == "__main__":
    sys.stdout.write(solution())
