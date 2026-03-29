import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    values = [0] + data[1:1 + n]
    edges_data = data[1 + n:]
    graph = [[] for _ in range(n + 1)]

    for i in range(0, len(edges_data), 2):
        u = edges_data[i]
        v = edges_data[i + 1]
        graph[u].append(v)
        graph[v].append(u)

    result = [False] * (n + 1)
    counts = {}
    repeated_values = 0
    stack = [(1, 0, 0)]

    while stack:
        vertex, parent, state = stack.pop()
        value = values[vertex]

        if state == 0:
            previous = counts.get(value, 0)
            counts[value] = previous + 1
            if previous + 1 == 2:
                repeated_values += 1

            result[vertex] = repeated_values > 0
            stack.append((vertex, parent, 1))

            for neighbor in reversed(graph[vertex]):
                if neighbor != parent:
                    stack.append((neighbor, vertex, 0))
        else:
            current = counts[value]
            if current == 2:
                repeated_values -= 1

            if current == 1:
                del counts[value]
            else:
                counts[value] = current - 1

    answer = ["YES" if value else "NO" for value in result[1:]]
    sys.stdout.write("\n".join(answer))


if __name__ == "__main__":
    main()
