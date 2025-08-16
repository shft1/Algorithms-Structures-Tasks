import sys


def create_adjacency_list(n, m):
    adj_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[v1].add(v2)
        adj_lst[v2].add(v1)
    return adj_lst


def DFS(start_vertex, count_comp, adj_lst, colors):
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        if colors[v] == -1:
            colors[v] = count_comp
            stack.append(v)
            for w in adj_lst[v]:
                if colors[w] == -1:
                    stack.append(w)


def search_conn_comp(adj_lst):
    colors = [-1] * len(adj_lst)
    count_comp = 0
    for i in range(1, len(colors)):
        if colors[i] == -1:
            count_comp += 1
            DFS(i, count_comp, adj_lst, colors)
    return count_comp, colors


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = create_adjacency_list(n, m)
    cnt_comp, colors = search_conn_comp(adj_lst)
    res = {i: [] for i in range(1, cnt_comp + 1)}
    for v in range(1, len(colors)):
        res[colors[v]].append(v)
    res = [list(map(str, el)) for el in sorted(res.values())]
    sys.stdout.write(f"{cnt_comp}\n")
    sys.stdout.write("\n".join(map(" ".join, res)))


if __name__ == "__main__":
    main()
