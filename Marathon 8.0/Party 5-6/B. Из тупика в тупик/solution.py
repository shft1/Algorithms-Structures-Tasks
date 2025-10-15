import sys
from collections import defaultdict
from queue import Queue


def multi_bfs(sources, adj_list):
    colors = defaultdict(lambda: "white")
    dist = defaultdict(int)
    parents = defaultdict(lambda: None)
    planned = Queue()
    for source in sources:
        planned.put(source)
        parents[source] = source
    min_dist = float("inf")
    while not planned.empty():
        v = planned.get()
        for w in adj_list[v]:
            if colors[w] == "white":
                colors[w] = "grey"
                dist[w] = dist[v] + 1
                parents[w] = parents[v]
                planned.put(w)
            elif colors[w] == "grey":
                if parents[w] != parents[v]:
                    min_dist = min(min_dist, dist[w] + dist[v] + 1)
        colors[v] = "black"
    return min_dist


def solution(adj_list, n):
    if n == 2:
        return 1
    sources = [key for key, value in adj_list.items() if len(value) == 1]
    return multi_bfs(sources, adj_list)


def main():
    n = int(sys.stdin.readline().rstrip())
    adj_list = defaultdict(set)
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj_list[a].add(b)
        adj_list[b].add(a)
    sys.stdout.write(str(solution(adj_list, n)))


if __name__ == "__main__":
    main()
