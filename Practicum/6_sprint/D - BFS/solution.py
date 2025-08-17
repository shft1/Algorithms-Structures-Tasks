import sys
from queue import Queue


def create_adjacency_list(n, m):
    adj_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[v1].add(v2)
        adj_lst[v2].add(v1)
    return adj_lst


def BFS(start_vertex, adj_lst):
    colors = ["white"] * len(adj_lst)
    planned = Queue()
    planned.put(start_vertex)
    colors[start_vertex] = "grey"
    res = []
    while not planned.empty():
        v = planned.get()
        for w in sorted(adj_lst[v]):
            if colors[w] == "white":
                colors[w] = "grey"
                planned.put(w)
        res.append(str(v))
        colors[v] = "black"
    return res


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = create_adjacency_list(n, m)
    s = int(sys.stdin.readline().rstrip())
    seq = BFS(s, adj_lst)
    sys.stdout.write(" ".join(seq))


if __name__ == "__main__":
    main()
