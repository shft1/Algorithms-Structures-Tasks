"""
ID посылки - https://contest.yandex.ru/contest/26133/run-report/143471113/

Задача:
Вывести наибольший общий префикс распакованных строк.

Примечание:
LCP - Longest Common Prefix (наибольший общий префикс)

--- Принцип работы ---
- Алгоритм распаковки строки:
    Итерироваться по строке и добавлять символы в массив, если встретили цифру,
    то рекурсивно запустить алгоритм для строки внутри скобок,
    базовый случай - это когда встретили закрывающуюся скобку,
    тогда происходит выход из рекурсии, передача указателя на продолжение и расширение массива строки.
- СПОСОБ №1
    Пусть length_p - длина LCP.
    Для начала, выберем, в качестве префикса, всю первую строку (length_p = len(s))
    Для каждой строки, будем сравнивать символы с шаблоном.
    Если они различаются на i индексе, то указатель length_p = i
    В конце вывести префикс после прохода (s[:length_p])
- СПОСОБ №2
    Создать префиксное дерево (бор) из первой строки, взять ее как за шаблон.
    Далее, каждая строка проходится по бору и отмечает на узле LCP.
    В конце алгоритм собирает узлы-символы, которые находятся до отметки LCP.
    Выводит наибольший общий префикс.

--- Доказательства корректности ---
Данный алгоритм опирается на транзитивное отношение (Если а = b и b = c, то а = с).
Если p1 - исходная строка, p2 - префикс p1, а p3 - префикс p2, то p3 префикс p1.
Исходя из этого свойства алгоритм корректен. ■

--- Временная сложность ---
Временная сложность алгоритма складывается из сложностей нескольких частей:
- Распаковка строк = O(K), где K - суммарная длина всех запакованных строк.
- Поиск LCP = O(L), где L - суммарная длина всех распакованных строк.
-> Итоговая временная сложность = O(K + L)

--- Пространственная сложность ---
Пространственная сложность алгоритма складывается из сложностей нескольких частей:
- Хранение стека вызовов при распаковки строк = O(M / 2) = O(M), где M - наибольшная длина строки
- Хранение наибольшего общего префикса = O(M), где M - наибольшная длина строки
-> Итоговая пространственная сложность = O(M + M) = O(M)
"""

import sys


def unpacking_string(string: str, start=0) -> str:
    unpacked_string: list[str] = []
    i: int = start
    while i < len(string):
        symb: str = string[i]
        if symb == "]":
            return unpacked_string, i + 1
        if symb.isdigit():
            part_uppacked, i = unpacking_string(string, i + 2)
            unpacked_string.extend(int(symb) * part_uppacked)
        else:
            unpacked_string.append(symb)
            i += 1
    return "".join(unpacked_string)


def solution(strings: list[str]) -> str:
    unpacked_strings: list[str] = [
        unpacking_string(string) for string in strings
    ]
    pattern: str = unpacked_strings[0]
    length_p: int = len(pattern)
    for string in unpacked_strings:
        length_s: int = len(string)
        i: int = 0
        while i < length_p and i < length_s:
            if string[i] != pattern[i]:
                length_p = i
            else:
                i += 1
        if i == length_s:
            length_p = i
    return pattern[:length_p]


def main() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    uppacked_string: list[str] = [
        sys.stdin.readline().rstrip() for _ in range(n)
    ]
    sys.stdout.write(solution(uppacked_string))


if __name__ == "__main__":
    main()


# ------------------------------------------------ СПОСОБ №2 ----------------------------------------------------

# import sys


# class TrieNode:
#     def __init__(self, symb="") -> None:
#         self.symb: str = symb
#         self.is_terminal: bool = False
#         self.next: TrieNode = None


# class Trie:
#     def __init__(self) -> None:
#         self.root: TrieNode = TrieNode()

#     def insert(self, string: str) -> None:
#         curr_node: TrieNode = self.root
#         for symb in string:
#             next_node = TrieNode(symb)
#             curr_node.next = next_node
#             curr_node = next_node
#         curr_node.is_terminal = True

#     def mark_LCP(self, prefix) -> None:
#         curr_node: TrieNode = self.root
#         for symb in prefix:
#             if curr_node.is_terminal:
#                 return
#             if symb != curr_node.next.symb:
#                 curr_node.is_terminal = True
#             else:
#                 curr_node: TrieNode = curr_node.next
#         curr_node.is_terminal = True

#     def find_LCP(self) -> str:
#         LCP: list[str] = []
#         curr_node = self.root
#         while not curr_node.is_terminal:
#             LCP.append(curr_node.symb)
#             curr_node = curr_node.next
#         LCP.append(curr_node.symb)
#         return "".join(LCP)


# def unpacking_string(string: str, start=0) -> str:
#     unpacked_string: list[str] = []
#     i: int = start
#     while i < len(string):
#         symb: str = string[i]
#         if symb == "]":
#             return unpacked_string, i + 1
#         if symb.isdigit():
#             part_uppacked, i = unpacking_string(string, i + 2)
#             unpacked_string.extend(int(symb) * part_uppacked)
#         else:
#             unpacked_string.append(symb)
#             i += 1
#     return "".join(unpacked_string)


# def solution(strings: list[str]) -> str:
#     trie: Trie = Trie()
#     trie.insert(unpacking_string(strings[0]))
#     for string in strings[1:]:
#         unpacked_string: str = unpacking_string(string)
#         trie.mark_LCP(unpacked_string)
#     return trie.find_LCP()


# def main():
#     n: int = int(sys.stdin.readline().rstrip())
#     strings: list[str] = [sys.stdin.readline().rstrip() for _ in range(n)]
#     sys.stdout.write(solution(strings))


# if __name__ == "__main__":
#     main()
