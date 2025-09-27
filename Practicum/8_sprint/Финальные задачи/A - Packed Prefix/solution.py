# Алгоритм распаковки: итерироваться по строке и добавлять символы в массив, если встретили цифру,
# то рекурсивно запустить алгоритм для строки внутри скобок,
# базовый случай когда мы встретили закрывающуюся скобку, тогда мы выходим из рекурсии и расширяем массив строки.

# Подготовка: Строку за строкой производить распаковку элементов и каждый из них добавлять в префиксное дерево.
# По пути добавления, в узле, сохранять кол-во строк которые удовлетворяют данному префиксу.

# Алгоритм: Взять, к примеру, первую строку как префикс, по которому мы будем идти по бору.
# Если в процессе итерации обнаруживается, что кол-во строк, удовлетворяющих этому префиксу меньше, чем всего строк,
# то наибольшая длина префикса будет равна i шагу (как длина от начала строки).


"""
ID посылки - https://contest.yandex.ru/contest/26133/run-report/143283584/
--- Принцип работы ---
--- Доказательства корректности ---
--- Временная сложность ---
--- Пространственная сложность ---
"""

import sys


class TrieNode:
    def __init__(self, symb="") -> None:
        self.symb: str = symb
        self.is_terminal: bool = False
        self.next: TrieNode = None


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, string: str) -> None:
        curr_node: TrieNode = self.root
        for symb in string:
            next_node = TrieNode(symb)
            curr_node.next = next_node
            curr_node = next_node
        curr_node.is_terminal = True

    def mark_LCP(self, prefix) -> None:
        curr_node: TrieNode = self.root
        for symb in prefix:
            if curr_node.is_terminal:
                return
            if symb != curr_node.next.symb:
                curr_node.is_terminal = True
            else:
                curr_node: TrieNode = curr_node.next
        curr_node.is_terminal = True

    def find_LCP(self) -> str:
        LCP: list[str] = []
        curr_node = self.root
        while not curr_node.is_terminal:
            LCP.append(curr_node.symb)
            curr_node = curr_node.next
        LCP.append(curr_node.symb)
        return "".join(LCP)


def unpacking_string(string: str, start=0) -> str:
    unpacked: list[str] = []
    i: int = start
    while i < len(string):
        symb: str = string[i]
        if symb == "]":
            return unpacked, i + 1
        if symb.isdigit():
            part_uppacked, i = unpacking_string(string, i + 2)
            unpacked.extend(int(symb) * part_uppacked)
        else:
            unpacked.append(symb)
            i += 1
    return "".join(unpacked)


def solution(strings: list[str]) -> str:
    trie: Trie = Trie()
    trie.insert(unpacking_string(strings[0]))
    for string in strings[1:]:
        unpacked: str = unpacking_string(string)
        trie.mark_LCP(unpacked)
    return trie.find_LCP()


def main():
    n: int = int(sys.stdin.readline().rstrip())
    strings: list[str] = [sys.stdin.readline().rstrip() for _ in range(n)]
    sys.stdout.write(solution(strings))


if __name__ == "__main__":
    main()

# Способ №2

# import sys


# def unpacking_string(string: str, start=0) -> str:
#     unpacked: list[str] = []
#     i: int = start
#     while i < len(string):
#         symb: str = string[i]
#         if symb == "]":
#             return unpacked, i + 1
#         if symb.isdigit():
#             part_uppacked, i = unpacking_string(string, i + 2)
#             unpacked.extend(int(symb) * part_uppacked)
#         else:
#             unpacked.append(symb)
#             i += 1
#     return "".join(unpacked)


# def solution(strings: list[str]) -> str:
#     unpacked_strings = [unpacking_string(string) for string in strings]
#     pattern = unpacked_strings[0]
#     length_p = len(pattern)
#     for string in unpacked_strings[1:]:
#         i = 0
#         while i < length_p and i < len(string):
#             if string[i] != pattern[i]:
#                 break
#             i += 1
#         pattern, length_p = string[:i], i
#     return "".join(pattern)


# def main() -> None:
#     n: int = int(sys.stdin.readline().rstrip())
#     strings: list[str] = [sys.stdin.readline().rstrip() for _ in range(n)]
#     sys.stdout.write(solution(strings))


# if __name__ == "__main__":
#     main()
