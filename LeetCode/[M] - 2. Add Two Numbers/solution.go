package main

// ListNode Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := &ListNode{}
	curr := &ListNode{Next: head}

	inMind := 0
	for l1 != nil && l2 != nil {
		curr = curr.Next
		curr.Next = &ListNode{}

		val := (inMind + l1.Val + l2.Val) % 10
		inMind = (inMind + l1.Val + l2.Val) / 10

		curr.Val = val

		l1 = l1.Next
		l2 = l2.Next
	}
	for l1 != nil {
		curr = curr.Next
		curr.Next = &ListNode{}

		val := (inMind + l1.Val) % 10
		inMind = (inMind + l1.Val) / 10

		curr.Val = val

		l1 = l1.Next
	}
	for l2 != nil {
		curr = curr.Next
		curr.Next = &ListNode{}

		val := (inMind + l2.Val) % 10
		inMind = (inMind + l2.Val) / 10

		curr.Val = val

		l2 = l2.Next
	}
	if inMind != 0 {
		curr = curr.Next
		curr.Val = inMind
	} else {
		curr.Next = nil
	}
	return head
}
