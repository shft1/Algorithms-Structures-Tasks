from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        marked = set([0])
        stack = [0]
        while stack:
            v = stack.pop()
            for w in rooms[v]:
                if w not in marked:
                    stack.append(w)
                    marked.add(w)
        return len(marked) == len(rooms)
