class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        wordCnt1 = {}
        for word in word1:
            wordCnt1[word] = wordCnt1.get(word, 0) + 1
        wordCnt2 = {}
        for word in word2:
            wordCnt2[word] = wordCnt2.get(word, 0) + 1
        if sorted(wordCnt1.values()) == sorted(wordCnt2.values()):
            return True
        return False
