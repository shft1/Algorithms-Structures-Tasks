import sys


def solution(n, m):
    list_smesh = [0] * (n + 1)
    for _ in range(m):
        out_e, in_e = map(int, sys.stdin.readline().split())
        if not list_smesh[out_e]:
            list_smesh[out_e] = {"pow_in": 0, "smesh_e": set()}
        list_smesh[out_e]["pow_in"] += 1
        list_smesh[out_e]["smesh_e"].add(in_e)
    return list_smesh


def main():
    n, m = map(int, sys.stdin.readline().split())
    list_smesh = solution(n, m)
    res = []
    for vrtx in list_smesh[1:]:
        if vrtx == 0:
            res.append("0")
        else:
            res_pow_in = str(vrtx["pow_in"])
            res_smesh = " ".join(map(str, sorted(vrtx["smesh_e"])))
            res.append(f"{res_pow_in} {res_smesh}")
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
