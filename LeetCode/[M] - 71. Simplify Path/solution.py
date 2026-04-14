class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for way in path.split("/"):
            if way != "." and way != "" and way != "..":
                stack.append(way)
            elif way == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)
