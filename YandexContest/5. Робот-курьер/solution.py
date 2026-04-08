import sys
from array import array
from heapq import heappop, heappush


def main():
    n = int(sys.stdin.readline().rstrip())

    cells = n * n
    grid = []
    for _ in range(n):
        grid.extend(list(map(int, sys.stdin.readline().rstrip().split())))

    start_idx = 0
    finish_idx = cells - 1
    if grid[start_idx] == -1 or grid[finish_idx] == -1:
        print(0)
        return

    station_pos = {}
    for idx, value in enumerate(grid):
        if value < -1:
            station_pos[value] = idx

    m = int(sys.stdin.readline().rstrip())
    connections = []
    active_station_ids = set()
    for _ in range(m):
        a, b = list(map(int, sys.stdin.readline().rstrip().split()))
        connections.append((a, b))
        active_station_ids.add(a)
        active_station_ids.add(b)

    active_station_ids = list(active_station_ids)
    id_to_dsu = {
        station_id: i for i, station_id in enumerate(active_station_ids)
    }
    parent_dsu = list(range(len(active_station_ids)))

    def find(x):
        while parent_dsu[x] != x:
            parent_dsu[x] = parent_dsu[parent_dsu[x]]
            x = parent_dsu[x]
        return x

    def union(x, y):
        rx = find(x)
        ry = find(y)
        if rx != ry:
            parent_dsu[ry] = rx

    for a, b in connections:
        union(id_to_dsu[a], id_to_dsu[b])

    metro_groups = {}
    for station_id in active_station_ids:
        root = find(id_to_dsu[station_id])
        metro_groups.setdefault(root, []).append(station_pos[station_id])

    node_count = cells * 2
    head = array("i", [-1]) * node_count
    to = array("i")
    nxt = array("i")
    cap = array("b")
    cost = array("q")

    def add_edge(u, v, capacity, edge_cost):
        to.append(v)
        nxt.append(head[u])
        cap.append(capacity)
        cost.append(edge_cost)
        head[u] = len(to) - 1

        to.append(u)
        nxt.append(head[v])
        cap.append(0)
        cost.append(-edge_cost)
        head[v] = len(to) - 1

    for idx, value in enumerate(grid):
        if value == -1:
            continue

        node_in = idx * 2
        node_out = node_in + 1
        reward = value if value > 0 else 0

        add_edge(node_in, node_out, 1, reward)
        add_edge(node_in, node_out, 1, 0)

        row = idx // n
        col = idx % n

        if col + 1 < n and grid[idx + 1] != -1:
            add_edge(node_out, (idx + 1) * 2, 2, 0)
        if row + 1 < n and grid[idx + n] != -1:
            add_edge(node_out, (idx + n) * 2, 2, 0)

    for stations in metro_groups.values():
        station_info = [(pos // n, pos % n, pos) for pos in stations]
        station_info.sort()
        length = len(station_info)
        for i in range(length):
            r1, c1, pos1 = station_info[i]
            out1 = pos1 * 2 + 1
            for j in range(i + 1, length):
                r2, c2, pos2 = station_info[j]
                if c1 <= c2:
                    add_edge(out1, pos2 * 2, 2, 0)

    source = start_idx * 2
    sink = finish_idx * 2 + 1

    neg_inf = -(10**30)
    dist = [neg_inf] * node_count
    prev_edge = [-1] * node_count
    dist[source] = 0

    for diag in range(2 * n - 1):
        row_from = max(0, diag - (n - 1))
        row_to = min(n - 1, diag)
        for row in range(row_from, row_to + 1):
            col = diag - row
            idx = row * n + col
            if grid[idx] == -1:
                continue
            node_in = idx * 2
            node_out = node_in + 1

            current = dist[node_in]
            if current != neg_inf:
                edge = head[node_in]
                while edge != -1:
                    if cap[edge]:
                        v = to[edge]
                        cand = current + cost[edge]
                        if cand > dist[v]:
                            dist[v] = cand
                            prev_edge[v] = edge
                    edge = nxt[edge]

            current = dist[node_out]
            if current != neg_inf:
                edge = head[node_out]
                while edge != -1:
                    if cap[edge]:
                        v = to[edge]
                        cand = current + cost[edge]
                        if cand > dist[v]:
                            dist[v] = cand
                            prev_edge[v] = edge
                    edge = nxt[edge]

    if dist[sink] == neg_inf:
        print(0)
        return

    answer = dist[sink]

    cur = sink
    while cur != source:
        edge = prev_edge[cur]
        cap[edge] -= 1
        cap[edge ^ 1] += 1
        cur = to[edge ^ 1]

    inf = 10**30
    dijkstra_dist = [inf] * node_count
    prev_edge = [-1] * node_count
    dijkstra_dist[source] = 0
    heap = [(0, source)]

    while heap:
        current_dist, u = heappop(heap)
        if current_dist != dijkstra_dist[u]:
            continue
        if u == sink:
            break

        potential_u = dist[u]
        edge = head[u]
        while edge != -1:
            if cap[edge]:
                v = to[edge]
                reduced_cost = dist[v] - potential_u - cost[edge]
                new_dist = current_dist + reduced_cost
                if new_dist < dijkstra_dist[v]:
                    dijkstra_dist[v] = new_dist
                    prev_edge[v] = edge
                    heappush(heap, (new_dist, v))
            edge = nxt[edge]

    if dijkstra_dist[sink] == inf:
        print(0)
        return

    cur = sink
    while cur != source:
        edge = prev_edge[cur]
        answer += cost[edge]
        cap[edge] -= 1
        cap[edge ^ 1] += 1
        cur = to[edge ^ 1]

    print(answer)


if __name__ == "__main__":
    main()
