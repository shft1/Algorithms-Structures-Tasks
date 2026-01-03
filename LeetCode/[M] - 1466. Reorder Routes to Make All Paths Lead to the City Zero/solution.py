import collections
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        paths = collections.defaultdict(set)
        for x, y in connections:
            paths[x].add(y)
            graph[x].add(y)
            graph[y].add(x)

        cnt = 0

        visited = set()
        stack = [0]
        while stack:
            v = stack.pop()
            visited.add(v)
            for w in graph[v]:
                if w not in visited:
                    stack.append(w)
                    if w in paths[v]:
                        cnt += 1
        return cnt
