import sys


def solution(s, t):
    """
    Time: O(n)
    Memory: O(n)
    """
    links = {}
    backlink = set()
    len_s, len_t = len(s), len(t)
    if len_s != len_t:
        return "NO"
    pointer_s, pointer_t = 0, 0
    while pointer_s < len_s and pointer_t < len_t:
        link_to = links.get(s[pointer_s])
        if link_to and link_to != t[pointer_t]:
            return "NO"
        if not link_to and t[pointer_t] in backlink:
            return "NO"
        if not link_to:
            links[s[pointer_s]] = t[pointer_t]
            backlink.add(t[pointer_t])
        pointer_s += 1
        pointer_t += 1
    return "YES"


def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(s, t) + "\n")


if __name__ == "__main__":
    main()
