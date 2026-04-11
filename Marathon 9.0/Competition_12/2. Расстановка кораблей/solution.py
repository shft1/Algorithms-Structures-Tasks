import sys


def main():
    grid = [sys.stdin.readline().rstrip() for _ in range(10)]
    if len(grid) != 10 or any(len(row) != 10 for row in grid):
        print("NO")
        return

    for row in range(10):
        for col in range(10):
            if grid[row][col] != "#":
                continue

            for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                nr = row + dr
                nc = col + dc
                if 0 <= nr < 10 and 0 <= nc < 10 and grid[nr][nc] == "#":
                    print("NO")
                    return

    visited = [[False] * 10 for _ in range(10)]
    ship_counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for row in range(10):
        for col in range(10):
            if grid[row][col] != "#" or visited[row][col]:
                continue

            stack = [(row, col)]
            visited[row][col] = True
            cells = []

            while stack:
                current_row, current_col = stack.pop()
                cells.append((current_row, current_col))

                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nr = current_row + dr
                    nc = current_col + dc
                    if (
                        0 <= nr < 10
                        and 0 <= nc < 10
                        and grid[nr][nc] == "#"
                        and not visited[nr][nc]
                    ):
                        visited[nr][nc] = True
                        stack.append((nr, nc))

            rows = {cell_row for cell_row, _ in cells}
            cols = {cell_col for _, cell_col in cells}

            if len(rows) > 1 and len(cols) > 1:
                print("NO")
                return

            size = len(cells)
            if size not in ship_counts:
                print("NO")
                return

            ship_counts[size] += 1

    if ship_counts == {1: 4, 2: 3, 3: 2, 4: 1}:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
