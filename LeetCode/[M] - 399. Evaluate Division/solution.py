import collections
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]],
    ) -> List[float]:
        adj_lst = self.create_adj_list(equations, values)
        res = []
        for start, end in queries:
            if start not in adj_lst or end not in adj_lst:
                res.append(-1)
                continue
            multi = 1
            for num in self.dfs(start, end, adj_lst):
                multi *= num
            res.append(multi)
        return res

    def create_adj_list(self, equations: List[List[str]], values: List[float]):
        adj_lst = collections.defaultdict(list)
        for i in range(len(equations)):
            x, y, w = equations[i][0], equations[i][1], values[i]
            adj_lst[x].append([y, w])
            adj_lst[y].append([x, 1 / w])
        return adj_lst

    def dfs(self, start, end, graph):
        stack = [[start, 1]]
        colors = {key: "white" for key in graph}
        way = []
        while stack:
            v, weight = stack.pop()
            if colors[v] == "white":
                colors[v] = "grey"
                way.append(weight)
                stack.append([v, weight])
                if v == end:
                    return way
                for w, weight in graph[v]:
                    if colors[w] == "white":
                        stack.append([w, weight])
            elif colors[v] == "grey":
                colors[v] = "black"
                way.pop()
        return [-1]
