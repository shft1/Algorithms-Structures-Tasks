package main

// ListNode - Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil || head.Next.Next == nil {
		return head
	}
	headEven := head.Next
	tailOdd, tailEven := head, headEven
	for tailEven != nil && tailEven.Next != nil {
		tailOdd.Next = tailOdd.Next.Next
		tailEven.Next = tailEven.Next.Next
		tailOdd = tailOdd.Next
		tailEven = tailEven.Next
	}
	tailOdd.Next = headEven
	return head
}
