package main

// HashMap + Double Linked List

type Node struct {
	key  int
	val  int
	prev *Node
	next *Node
}

type LRUCache struct {
	head *Node
	tail *Node
	kv   map[int]*Node
	size int
}

func Constructor(capacity int) LRUCache {
	head, tail := &Node{}, &Node{}
	head.next = tail
	head.next.prev = head
	return LRUCache{
		head: head,
		tail: tail,
		kv:   make(map[int]*Node, capacity),
		size: capacity,
	}
}

func (lru *LRUCache) Get(key int) int {
	elem, ok := lru.kv[key]
	if !ok {
		return -1
	}
	lru.promote(elem)
	return elem.val
}

func (lru *LRUCache) Put(key int, value int) {
	elem, ok := lru.kv[key]
	if !ok {
		elem = &Node{key: key, val: value}
		lru.kv[key] = elem
		if len(lru.kv) > lru.size {
			delete(lru.kv, lru.tail.prev.key)
			lru.detach(lru.tail.prev)
		}
	}
	elem.val = value
	lru.promote(elem)
}

func (lru *LRUCache) promote(node *Node) {
	if node.prev != nil {
		lru.detach(node)
	}
	node.next = lru.head.next
	node.prev = lru.head
	node.prev.next = node
	node.next.prev = node
}

func (lru *LRUCache) detach(node *Node) {
	next := node.next
	prev := node.prev
	node.prev.next = next
	node.next.prev = prev
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
