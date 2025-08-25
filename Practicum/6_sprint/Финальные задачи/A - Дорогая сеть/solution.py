import sys
from heapq import heappop, heappush


def create_adjacency_list(n, m):
    adj_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        v1, v2, weight = map(int, sys.stdin.readline().rstrip().split())
        adj_lst[v1].add((-weight, v2))
        adj_lst[v2].add((-weight, v1))
    return adj_lst


def max_spt(adj_lst, start_vertex=1):
    visited = set()
    heap = []
    heappush(heap, (0, start_vertex))
    max_weight = 0
    while heap:
        weight, to_v = heappop(heap)
        if to_v not in visited:
            visited.add(to_v)
            max_weight += weight
            for adj_edge in adj_lst[to_v]:
                heappush(heap, adj_edge)
    if len(visited) == len(adj_lst) - 1:
        return str(-max_weight)
    return "Oops! I did it again"


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_lst = create_adjacency_list(n, m)
    weight_mx_spt = max_spt(adj_lst)
    sys.stdout.write(weight_mx_spt)


if __name__ == "__main__":
    main()
