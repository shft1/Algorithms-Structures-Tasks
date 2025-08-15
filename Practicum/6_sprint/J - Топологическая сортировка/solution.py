import sys


def create_dependency_list(n, m):
    """
    Time: O(V + E)
    Memory: O(V + E)
    """
    depend_lst = [set() for _ in range(n + 1)]
    for _ in range(m):
        frm_edge, to_edge = map(int, sys.stdin.readline().rstrip().split())
        depend_lst[to_edge].add(frm_edge)
    return depend_lst


def top_sort(start_vertex, depend_lst, colors):
    stack = [start_vertex]
    order = []
    while stack:
        v = stack.pop()
        if colors[v] == "white":
            colors[v] = "grey"
            stack.append(v)
            for w in depend_lst[v]:
                if colors[w] == "white":
                    stack.append(w)
        elif colors[v] == "grey":
            colors[v] = "black"
            order.append(v)
    return order


def main_top_sort(depend_lst):
    res = []
    colors = ["white"] * len(depend_lst)
    for i in range(1, len(colors)):
        if colors[i] == "white":
            res.extend(top_sort(i, depend_lst, colors))
    return res


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    depend_lst = create_dependency_list(n, m)
    res = main_top_sort(depend_lst)
    sys.stdout.write(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
