from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            wordS = "".join(sorted(list(word)))
            if wordS in group:
                group[wordS].append(word)
            else:
                group[wordS] = [word]

        return list(group.values())
