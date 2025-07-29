import sys


class MinHeap:
    def __init__(self, size, func_key=lambda x: x) -> None:
        self.size = size
        self.last_idx = 0
        self.func_key = func_key
        self.heap = [None] * (self.size + 1)

    def _sift_up(self, idx: int) -> None:
        if idx == 1:
            return
        p_idx = idx // 2
        if self.func_key(self.heap[idx]) < self.func_key(self.heap[p_idx]):
            self.heap[p_idx], self.heap[idx] = self.heap[idx], self.heap[p_idx]
            self._sift_up(p_idx)

    def add(self, obj) -> None:
        if self.last_idx == self.size:
            raise RuntimeError("Куча переполнена!")
        self.last_idx += 1
        self.heap[self.last_idx] = obj
        self._sift_up(self.last_idx)

    def _sift_down(self, idx: int) -> None:
        l_idx = idx * 2
        if l_idx > self.last_idx:
            return
        if l_idx < self.last_idx and self.func_key(
            self.heap[l_idx + 1]
        ) < self.func_key(self.heap[l_idx]):
            min_idx = l_idx + 1
        else:
            min_idx = l_idx
        if self.func_key(self.heap[min_idx]) < self.func_key(self.heap[idx]):
            self.heap[min_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[min_idx],
            )
            self._sift_down(min_idx)

    def pop_max(self) -> list[str]:
        if self.last_idx == 0:
            raise RuntimeError("Куча пуста!")
        max_obj = self.heap[1]
        self.heap[1] = self.heap[self.last_idx]
        self.heap[self.last_idx] = None
        self.last_idx -= 1
        self._sift_down(1)
        return max_obj


def func_key(obj) -> tuple:
    return (-int(obj[1]), int(obj[2]), obj[0])


def heap_sort(n: int) -> list[str]:
    heap = MinHeap(size=n, func_key=func_key)
    try:
        for _ in range(n):
            obj = sys.stdin.readline().rstrip().split()
            heap.add(obj)
        return [heap.pop_max()[0] for _ in range(n)]
    except RuntimeError as e:
        return f"Ошибка-при-работе-с-кучей--->{e}"


def main():
    n: int = int(sys.stdin.readline().rstrip())
    res: list[str] = heap_sort(n)
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
