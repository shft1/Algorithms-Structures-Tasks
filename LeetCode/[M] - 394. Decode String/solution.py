class Solution:
    def decodeString(self, s: str) -> str:
        decode, multi = [], []
        for si in s:
            if si.isdigit():
                multi.append(si)
            elif si == "[":
                decode.append("".join(multi))
                multi = []
            elif si == "]":
                inter = []
                while decode[-1].isalpha():
                    inter.append(decode.pop())
                decode.extend(reversed(inter * int(decode.pop())))
            else:
                decode.append(si)
        return "".join(decode)
