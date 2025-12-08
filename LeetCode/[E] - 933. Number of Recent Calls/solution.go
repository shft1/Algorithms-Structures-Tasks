package main

type RecentCounter struct {
	queue []int
	head  int
}

func Constructor() RecentCounter {
	return RecentCounter{queue: []int{}}
}

func (rc *RecentCounter) Ping(t int) int {
	rc.queue = append(rc.queue, t)
	for rc.queue[rc.head] < t-3000 {
		rc.head++
	}
	return len(rc.queue) - rc.head
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */
