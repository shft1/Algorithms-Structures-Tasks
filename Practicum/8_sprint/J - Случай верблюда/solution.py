import sys


class Node:
    def __init__(self):
        self.childs: dict = {}
        self.class_name: list = []


class Trie:
    def __init__(self):
        self.root: Node = Node()

    def insert(self, uppercase_seq, class_name):
        curr_node = self.root
        curr_node.class_name.append(class_name)
        for upp_char in uppercase_seq:
            if upp_char not in curr_node.childs:
                curr_node.childs[upp_char] = Node()
            curr_node = curr_node.childs[upp_char]
            curr_node.class_name.append(class_name)

    def search_by_prefix(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.childs:
                return []
            curr_node = curr_node.childs[char]
        return curr_node.class_name


def extract_uppercase_seq(seq):
    return "".join(char for char in seq if char.isupper())


def solution(classes, patterns):
    trie = Trie()
    for class_name in classes:
        trie.insert(extract_uppercase_seq(class_name), class_name)
    res = []
    for pattern in patterns:
        curr_pattern = trie.search_by_prefix(pattern)
        curr_pattern.sort()
        res.extend(curr_pattern)
    return res


def main():
    n = int(sys.stdin.readline().rstrip())
    classes = [sys.stdin.readline().rstrip() for _ in range(n)]
    m = int(sys.stdin.readline().rstrip())
    patterns = [sys.stdin.readline().rstrip() for _ in range(m)]
    sys.stdout.write("\n".join(solution(classes, patterns)))


if __name__ == "__main__":
    main()
