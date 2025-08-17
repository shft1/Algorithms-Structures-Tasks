import sys
from queue import Queue


def create_adjacency_list(n, m):
    adj_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[v1].add(v2)
        adj_lst[v2].add(v1)
    return adj_lst


def DFS(start_vertex, adj_lst):
    colors = ["white"] * len(adj_lst)
    planned = Queue()
    planned.put(start_vertex)
    colors[start_vertex] = "grey"
    dist = [None] * len(adj_lst)
    dist[start_vertex] = 0
    while not planned.empty():
        v = planned.get()
        for w in adj_lst[v]:
            if colors[w] == "white":
                colors[w] = "grey"
                dist[w] = dist[v] + 1
                planned.put(w)
        colors[v] = "black"
    return dist[1:]


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = create_adjacency_list(n, m)
    s = int(sys.stdin.readline().rstrip())
    distances = DFS(s, adj_lst)
    sys.stdout.write(str(max(distances)))


if __name__ == "__main__":
    main()
