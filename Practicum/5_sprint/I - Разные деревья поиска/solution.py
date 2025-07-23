import sys


def solution(n):
    # numTree [4] = numTree[0] * numTree[3] +
    #               numTree [1] * numTree[2] +
    #               numTree [2] * numTree[1] +
    #               numTree [3] * numTree [0]
    numsTree = [1] * (n + 1)  # результаты подзадач
    for nodes in range(2, n + 1):  # считаю каждую подзадачу
        total = 0
        for root in range(1, nodes + 1):  # считаю подзадачу как задачу
            left = root - 1
            right = nodes - root
            total += numsTree[left] * numsTree[right]
        numsTree[nodes] = total
    return numsTree[n]  # последняя подзадача - это основная задача


def main():
    n = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(solution(n)))


if __name__ == "__main__":
    main()
