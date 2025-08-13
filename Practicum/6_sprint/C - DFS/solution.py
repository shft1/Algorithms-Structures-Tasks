import sys


def create_adjacency_list(n, m):
    adj_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        out_edge, in_edge = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[out_edge].add(in_edge)
        adj_lst[in_edge].add(out_edge)
    return adj_lst


def DFS(start_vertex, adj_lst):
    res = []
    colors = ["white"] * len(adj_lst)
    stack = [start_vertex]

    while stack:
        v = stack.pop()
        if colors[v] == "white":
            colors[v] = "gray"
            stack.append(v)
            res.append(str(v))
            for w in sorted(adj_lst[v], reverse=True):
                if colors[w] == "white":
                    stack.append(w)
        elif colors[v] == "gray":
            colors[v] = "black"
    return res


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = create_adjacency_list(n, m)
    start_vertex = int(sys.stdin.readline().rstrip())
    res = DFS(start_vertex, adj_lst)
    sys.stdout.write(" ".join(res))


if __name__ == "__main__":
    main()
