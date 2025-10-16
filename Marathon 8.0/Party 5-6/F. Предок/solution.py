import sys


def dfs(start_v, tree, n):
    colors = ["white"] * (n + 1)
    time = 0
    tin, tout = [0] * (n + 1), [0] * (n + 1)
    stack = []
    stack.append(start_v)
    while stack:
        v = stack.pop()
        if colors[v] == "white":
            colors[v] = "grey"
            time += 1
            tin[v] = time
            stack.append(v)
            for w in tree[v]:
                if colors[w] == "white":
                    stack.append(w)
        elif colors[v] == "grey":
            colors[v] = "black"
            time += 1
            tout[v] = time
    return tin, tout


def solution(n):
    tree = [[] for _ in range(n + 1)]
    parents = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(0, n):
        parent, children = parents[i], i + 1
        tree[parent].append(children)
    tin, tout = dfs(0, tree, n)
    m = int(sys.stdin.readline().rstrip())
    res = [None] * (m)
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        res[i] = [0, 1][tin[b] > tin[a] and tout[b] < tout[a]]
    return res


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write("\n".join(map(str, solution(n))))


if __name__ == "__main__":
    main()
