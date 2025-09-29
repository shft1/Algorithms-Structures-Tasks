"""
ID посылки - https://contest.yandex.ru/contest/26133/run-report/143472066/

Задача:
Дан текст T и набор слов. Нужно определить, можно ли разбить T на последовательность слов из словаря,
стоит отметить, что слова можно использовать многократно и в любом порядке.

--- Принцип работы ---
В данной задачи используется бор (префиксное дерево) для одновременной проверки всех строк разбиения.
Идея строится на методе динамического программирования, с обратным ходом.
Состояние динамики, dp[i], описывает возможность разбиения строки T[i:].
Базовый случай динамики - пустая строка, т.е dp[len(T)] = YES.
Далее алгоритм идет обратным ходом, и для каждого T[i:] ищет такой префикс в боре,
который является строкой разбиения и который позволяет разбить строку после него.
Итоговый результат для всей строки T, будет содержаться в dp[0]

--- Доказательства корректности ---
Докажем корректность работы алгоритма по методу математической индукции:
- Введем понятие базы индукции:
    База индукции - dp[len(T)] = "YES", поскольку пустую строку мы всегда можем составить и без слов.
- Далее докажем шаг индукции:
    Предположим, что T[i : i + с] - строка разбиения, а dp[i + c] - возможность разбиения строки T[i + c: ],
    тогда, для того, чтобы узнать возможность разбиения строки T[i:] достаточно проверить только утверждение,
    что возможно разбить строку T[i + c: ], т.е. значение dp[i + c], поскольку мы точно знаем,
    что T[i : i + с] - строка разбиения. Если же T[i : i + с] - НЕ строка разбиения, то разбить строку нельзя
- База индукции есть, Шаг индукции доказан -> Алгоритм корректен. ■

--- Временная сложность ---
Временная сложность алгоритма складывается из сложностей нескольких частей:
- Построение префиксного дерева (бора) для строк разбиения:
    O(L), где L - сумма всех символов строк разбиения
- Вычисление динамики:
    O(M ^ 2), где M - длина исходной строки
-> Итоговая временная сложность алгоритма = O(L + M^2) = O(M^2) (тк как M^2 принимает большее значение)

--- Пространственная сложность ---
Пространственная сложность алгоритма складывается из сложностей нескольких частей:
- Хранение префиксного дерева (бора) для строк разбиения:
    O(L * 26), где L - сумма всех символов строк разбиения,
    а 26 (мощность английского алфавита) - максимальное кол-во дочерних элементов узла, т.е размер хеш-таблицы
    В силу асимптотики = O(L)
- Хранение состояний динамики:
    O(M), где M - длина исходной строки
-> Итоговая пространственная сложность алгоритма = O(L + M)
"""

import sys


class TrieNode:
    def __init__(self) -> None:
        self.is_terminal: bool = False
        self.children: dict[str, TrieNode] = {}
        self.length_prfx: int = 0


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for symb in word:
            if symb not in curr_node.children:
                curr_node.children[symb] = TrieNode()
            curr_node: TrieNode = curr_node.children[symb]
        curr_node.is_terminal = True
        curr_node.length_prfx = len(word)


def solution(cheapsheet: str, words: list[str]) -> str:
    length_chsh: int = len(cheapsheet)
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)
    dp: list[bool] = [False] * (length_chsh + 1)
    dp[-1] = True
    for i in range(length_chsh - 1, -1, -1):
        curr_node: TrieNode = trie.root
        j: int = i
        while j < length_chsh and cheapsheet[j] in curr_node.children:
            curr_node: TrieNode = curr_node.children[cheapsheet[j]]
            if curr_node.is_terminal:
                dp[i] = dp[i + curr_node.length_prfx]
            if dp[i]:
                break
            j += 1
    return "YES" if dp[0] else "NO"


def main() -> None:
    cheapsheet: str = sys.stdin.readline().rstrip()
    n: int = int(sys.stdin.readline().rstrip())
    words: list[str] = [sys.stdin.readline().rstrip() for _ in range(n)]
    sys.stdout.write(solution(cheapsheet, words))


if __name__ == "__main__":
    main()
