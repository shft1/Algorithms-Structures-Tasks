import sys

sys.setrecursionlimit(10**9)


def street_going(v, prev, adj_list, queues, population):
    for w in adj_list[v][1]:
        if w != prev:
            queues[v].append(street_going(w, v, adj_list, queues, population))
    sum_people = sum(queues[v])
    queues[v].append(population - sum_people)
    return sum_people


def solution(n, p):
    population = sum(p)
    adj_list = [(None, [])] + [[p[i], []] for i in range(n)]
    queues = {i: [p[i - 1]] for i in range(1, n + 1)}
    for _ in range(n - 1):
        v, w = map(int, sys.stdin.readline().rstrip().split())
        adj_list[v][1].append(w)
        adj_list[w][1].append(v)
    street_going(1, 0, adj_list, queues, population)
    res, min_max = None, float("inf")
    for square, queue in queues.items():
        min_max = min(min_max, max(queue))
        res = square if min(min_max, max(queue)) == max(queue) else res
    return res


def main():
    n = int(sys.stdin.readline().rstrip())
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, p)))


if __name__ == "__main__":
    main()
