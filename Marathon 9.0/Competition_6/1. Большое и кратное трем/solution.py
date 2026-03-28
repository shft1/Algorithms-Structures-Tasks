def main():
    s = input().strip()
    if len(s) < 3:
        print(-2)
        return

    counts = [0] * 10
    total_sum = 0
    for ch in s:
        d = ord(ch) - ord("0")
        counts[d] += 1
        total_sum += d

    rem = total_sum % 3

    mod1_digits = [1, 4, 7]
    mod2_digits = [2, 5, 8]

    def remove_smallest(rem_group, k):
        removed = [0] * 10
        need = k
        for d in rem_group:
            if need == 0:
                break
            take = min(counts[d], need)
            removed[d] = take
            need -= take
        if need != 0:
            return None
        return removed

    def build_candidate(removed):
        if removed is None:
            return None
        parts = []
        for d in range(9, -1, -1):
            cnt = counts[d] - removed[d]
            if cnt > 0:
                parts.append(str(d) * cnt)
        return "".join(parts)

    def better(a, b):
        if a is None:
            return b
        if b is None:
            return a

        ac = a.lstrip("0") or "0"
        bc = b.lstrip("0") or "0"

        if len(ac) != len(bc):
            return a if len(ac) > len(bc) else b
        if ac != bc:
            return a if ac > bc else b
        return a if len(a) >= len(b) else b

    if rem == 0:
        print(build_candidate([0] * 10))
        return

    if rem == 1:
        cand1 = build_candidate(remove_smallest(mod1_digits, 1))
        cand2 = build_candidate(remove_smallest(mod2_digits, 2))
        print(better(cand1, cand2))
        return

    cand1 = build_candidate(remove_smallest(mod2_digits, 1))
    cand2 = build_candidate(remove_smallest(mod1_digits, 2))
    print(better(cand1, cand2))


if __name__ == "__main__":
    main()
