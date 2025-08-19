import sys


def create_adjacency_matrix(n, m):
    adj_mtrx = [[-1 if j != i else 0 for j in range(n)] for i in range(n)]
    for _ in range(m):
        v1, v2, weight = map(int, sys.stdin.readline().rstrip().split())
        if adj_mtrx[v1 - 1][v2 - 1] == -1 or adj_mtrx[v1 - 1][v2 - 1] > weight:
            adj_mtrx[v1 - 1][v2 - 1] = weight
            adj_mtrx[v2 - 1][v1 - 1] = weight
    return adj_mtrx


def relax(v, w, dist, adj_mtrx):
    if dist[v] + adj_mtrx[v][w] < dist[w]:
        dist[w] = dist[v] + adj_mtrx[v][w]


def get_min_dist_not_visited_vertex(visited, dist, size_v):
    curr_min = float("inf")
    curr_min_v = -1
    for vi in range(size_v):
        if not visited[vi] and dist[vi] < curr_min:
            curr_min = dist[vi]
            curr_min_v = vi
    return curr_min_v


def dijkstra(s, adj_mtrx, size_v):
    visited = [False] * size_v
    dist = [float("inf")] * size_v

    dist[s] = 0

    while True:
        # Находим ещё непосещённую вершину с минимальным расстоянием от s.
        v = get_min_dist_not_visited_vertex(visited, dist, size_v)

        # Либо мы посетили все вершины, либо осталась недостижимая вершина
        if v == -1 or dist[v] == float("inf"):
            break

        # Когда вершина посещается, в ней уже записано оптимальное расстояние
        visited[v] = True

        # Запускаем процедуру релаксации для смежных вершин
        for w in range(size_v):
            if adj_mtrx[v][w] != -1:
                relax(v, w, dist, adj_mtrx)

    return dist


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_mtrx = create_adjacency_matrix(n, m)
    len_mtrx = [" ".join(map(str, dijkstra(s, adj_mtrx, n))) for s in range(n)]
    sys.stdout.write("\n".join([s.replace("inf", "-1") for s in len_mtrx]))


if __name__ == "__main__":
    main()
