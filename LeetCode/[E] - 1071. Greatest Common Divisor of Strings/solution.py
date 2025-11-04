class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len_str1, len_str2 = len(str1), len(str2)
        for i in range(min(len_str1, len_str2), -1, -1):
            if len_str1 % (i + 1) == 0 and len_str2 % (i + 1) == 0:
                cand = str1[: i + 1]
                div1 = str1.split(cand)
                div2 = str2.split(cand)
                if "".join(div1) == "".join(div2) == "":
                    return cand
        return ""
