import sys


def DFS(y, x, vectors, islands, n, m, card):
    area = 0
    stack = [(y, x)]
    while stack:
        point = stack.pop()
        py, px = point
        if card[py][px] == "#":
            area += 1
            card[py][px] = islands
            for vy, vx in vectors:
                neighbour = (py + vy, px + vx)
                ny, nx = neighbour
                if 0 <= ny < n and 0 <= nx < m and card[ny][nx] == "#":
                    stack.append(neighbour)
    return area


def solution(n, m, card):
    vectors = ((0, 1), (0, -1), (1, 0), (-1, 0))
    islands = 0
    mx_count_islands = 0
    for y in range(n):
        for x in range(m):
            if card[y][x] == "#":
                islands += 1
                area = DFS(y, x, vectors, islands, n, m, card)
                mx_count_islands = max(area, mx_count_islands)
    return islands, mx_count_islands


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    card = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    cnt_comp, mx_cnt_islnds = solution(n, m, card)
    sys.stdout.write(f"{cnt_comp} {mx_cnt_islnds}")


if __name__ == "__main__":
    main()
