import sys


def main():
    sys.setrecursionlimit(60000)
    s = input()
    n = len(s)

    memo = {}

    def parse_value(i):
        if i in memo:
            return memo[i]
        memo[i] = -1
        if i >= n:
            return -1
        c = s[i]
        if c == '"':
            memo[i] = parse_string(i)
        elif c == "{":
            memo[i] = parse_object(i)
        elif c == "[":
            memo[i] = parse_array(i)
        elif c.isdigit() or (c == "-" and i + 1 < n and s[i + 1].isdigit()):
            memo[i] = parse_integer(i)
        return memo[i]

    def parse_string(i):
        j = i + 1
        while j < n:
            c = s[j]
            if c == "\\":
                j += 2
                if j > n:
                    return -1
            elif c == '"':
                return j + 1
            else:
                j += 1
        return -1

    def parse_integer(i):
        j = i
        if s[j] == "-":
            j += 1
        if s[j] == "0":
            return j + 1
        while j < n and s[j].isdigit():
            j += 1
        return j

    def skip_ws(j):
        while j < n and s[j] == " ":
            j += 1
        return j

    def parse_object(i):
        j = skip_ws(i + 1)
        if j < n and s[j] == "}":
            return j + 1
        while True:
            j = skip_ws(j)
            if j >= n or s[j] != '"':
                return -1
            j = parse_string(j)
            if j == -1:
                return -1
            j = skip_ws(j)
            if j >= n or s[j] != ":":
                return -1
            j = skip_ws(j + 1)
            j = parse_value(j)
            if j == -1:
                return -1
            j = skip_ws(j)
            if j < n and s[j] == "}":
                return j + 1
            if j >= n or s[j] != ",":
                return -1
            j += 1

    def parse_array(i):
        j = skip_ws(i + 1)
        if j < n and s[j] == "]":
            return j + 1
        while True:
            j = skip_ws(j)
            j = parse_value(j)
            if j == -1:
                return -1
            j = skip_ws(j)
            if j < n and s[j] == "]":
                return j + 1
            if j >= n or s[j] != ",":
                return -1
            j += 1

    dp = [0] * (n + 1)
    took = [False] * n
    end_at = [0] * n

    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1]
        e = parse_value(i)
        if e != -1:
            val = (e - i) + dp[e]
            if val > dp[i]:
                dp[i] = val
                took[i] = True
                end_at[i] = e

    intervals = []
    i = 0
    while i < n:
        if took[i]:
            intervals.append((i, end_at[i]))
            i = end_at[i]
        else:
            i += 1

    print(len(intervals), dp[0])
    for l, r in intervals:
        print(l, r)


main()
