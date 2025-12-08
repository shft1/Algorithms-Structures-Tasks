class RecentCounter:
    def __init__(self):
        self.queue = []
        self.head = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[self.head] < t - 3000:
            self.head += 1
        return len(self.queue) - self.head



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)