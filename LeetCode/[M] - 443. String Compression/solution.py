class Solution:
    def compress(self, chars: list[str]) -> int:
        p_symb, p_cnt = 0, 0
        res = 0
        while p_cnt != len(chars):
            ch_s, ch_cnt = chars[p_symb], chars[p_cnt]
            if ch_s == ch_cnt:
                p_cnt += 1
                res += 1
            else:
                if res < 2:
                    p_symb += 1
                    chars[p_symb] = chars[p_cnt]
                else:
                    p_symb += 1
                    for char in str(res):
                        chars[p_symb] = char
                        p_symb += 1
                    chars[p_symb] = chars[p_cnt]
                res = 0
        if res < 2:
            return p_symb + 1
        p_symb += 1
        for char in str(res):
            chars[p_symb] = char
            p_symb += 1
        return p_symb
