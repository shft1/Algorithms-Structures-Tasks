from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt, visited = 0, set()
        for v in range(len(isConnected)):
            if v not in visited:
                cnt += 1
                self.dfs(v, visited, isConnected)
        return cnt

    def dfs(self, start_vertex, visited, isConnected):
        stack = [start_vertex]
        while stack:
            v = stack.pop()
            visited.add(v)
            for w in range(len(isConnected[v])):
                if w not in visited and isConnected[v][w]:
                    stack.append(w)
