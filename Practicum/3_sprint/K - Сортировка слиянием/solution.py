def merge(arr, lf, mid, rg):
    if rg - lf <= 1:
        return [arr[lf]]

    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    res = [0] * (rg - lf)

    fixed_mid, k = mid, 0
    while lf < fixed_mid and mid < rg:
        if arr[lf] <= arr[mid]:
            res[k] = arr[lf]
            lf += 1
        else:
            res[k] = arr[mid]
            mid += 1
        k += 1

    while lf < fixed_mid:
        res[k] = arr[lf]
        lf += 1
        k += 1

    while mid < rg:
        res[k] = arr[mid]
        mid += 1
        k += 1

    return res


def merge_sort(arr, lf, rg):
    arr[lf:rg] = merge(arr, lf, (rg + lf) // 2, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
