"""
ID посылки - https://contest.yandex.ru/contest/26133/run-report/143283584/
--- Принцип работы ---
--- Доказательства корректности ---
--- Временная сложность ---
--- Пространственная сложность ---
"""

import sys


class TrieNode:
    def __init__(self) -> None:
        self.is_terminal: bool = False
        self.child: dict[str, TrieNode] = {}
        self.length_prfx: int = 0


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        curr_node: TrieNode = self.root
        for symb in word:
            if symb not in curr_node.child:
                curr_node.child[symb] = TrieNode()
            curr_node: TrieNode = curr_node.child[symb]
        curr_node.is_terminal = True
        curr_node.length_prfx = len(word)


def solution(cheepsheet: str, words: list[str]) -> str:
    length_chsh: int = len(cheepsheet)
    trie: Trie = Trie()
    for word in words:
        trie.insert(word)
    dp: list[str] = ["NO"] * (length_chsh + 1)
    dp[-1] = "YES"
    for i in range(length_chsh - 1, -1, -1):
        curr_node: TrieNode = trie.root
        for symb in cheepsheet[i:]:
            if symb not in curr_node.child:
                break
            curr_node: TrieNode = curr_node.child[symb]
            if curr_node.is_terminal:
                dp[i] = dp[i + curr_node.length_prfx]
            if dp[i] == "YES":
                break
    return dp[0]


def main() -> None:
    cheepsheet: str = sys.stdin.readline().rstrip()
    n: int = int(sys.stdin.readline().rstrip())
    words: list[str] = [sys.stdin.readline().rstrip() for _ in range(n)]
    sys.stdout.write(solution(cheepsheet, words))


if __name__ == "__main__":
    main()
