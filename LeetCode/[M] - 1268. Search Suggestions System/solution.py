from typing import List


class Node:
    def __init__(self):
        self.words = []
        self.childrens = {}


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        root = Node()
        node = root
        for product in products:
            for char in product:
                if char not in node.childrens:
                    node.childrens[char] = Node()
                node = node.childrens[char]
                node.words.append(product)
            node = root

        res = [[] for _ in range(len(searchWord))]
        for i in range(len(searchWord)):
            if searchWord[i] not in node.childrens:
                return res
            node = node.childrens[searchWord[i]]
            res[i] = node.words[:3]

        return res
