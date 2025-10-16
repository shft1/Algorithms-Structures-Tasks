import sys


def dfs(node, tree, values):
    pos, neg = 0, 0
    for children in tree[node]:
        ch_pos, ch_neg = dfs(children, tree, values)
        pos += ch_pos
        neg += ch_neg
    value = values[node] + pos - neg
    if value > 0:
        neg += value
    else:
        pos += -value
    return pos, neg


def solution(tree, values):
    pos, neg = dfs(0, tree, values)
    return pos + neg


def main():
    n = int(sys.stdin.readline().rstrip())
    tree = [[] for _ in range(n)]
    for i in range(1, n):
        parent = int(sys.stdin.readline().rstrip())
        tree[parent].append(i)
    values = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(tree, values)))


if __name__ == "__main__":
    main()
