import sys


def create_adjacency_list(n, m):
    adj_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        frm, to = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[frm].add(to)
    return adj_lst


def DFS(adj_lst, start_vertex=1):
    colors = ["white"] * len(adj_lst)
    time = -1
    entry, leave = [-1] * len(adj_lst), [-1] * len(adj_lst)
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if colors[v] == "white":
            colors[v] = "grey"
            time += 1
            entry[v] = time
            stack.append(v)
            for w in sorted(adj_lst[v], reverse=True):
                if colors[w] == "white":
                    stack.append(w)
        elif colors[v] == "grey":
            colors[v] = "black"
            time += 1
            leave[v] = time
    return entry, leave


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = create_adjacency_list(n, m)
    entry, leave = DFS(adj_lst)
    res = [f"{entry[i]} {leave[i]}" for i in range(1, n + 1)]
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
