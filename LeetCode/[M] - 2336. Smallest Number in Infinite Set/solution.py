class SmallestInfiniteSet:
    def __init__(self):
        self.is_delete = [False] * 1001
        self.heap = [-1]
        self.next = 1

    def popSmallest(self) -> int:
        if len(self.heap) > 1:
            smallest = self.heap[1]
            leaf = self.heap.pop()
            if len(self.heap) > 1:
                self.heap[1] = leaf
                self.sift_down()
            self.is_delete[smallest] = True
            return smallest
        else:
            smallest = self.next
            self.next += 1
            self.is_delete[smallest] = True
            return smallest

    def addBack(self, num: int) -> None:
        if not self.is_delete[num]:
            return
        if num < self.next:
            self.heap.append(num)
            self.sift_up()
        self.is_delete[num] = False

    def sift_down(self):
        idx = 1
        n = len(self.heap)
        while True:
            left = idx * 2
            right = left + 1
            smallest = idx
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self.heap[idx], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[idx],
            )
            idx = smallest

    def sift_up(self):
        idx = len(self.heap) - 1
        while idx > 1:
            parent = idx // 2
            if self.heap[idx] >= self.heap[parent]:
                break
            self.heap[idx], self.heap[parent] = (
                self.heap[parent],
                self.heap[idx],
            )
            idx = parent
