package main

// ListNode - Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func pairSum(head *ListNode) int {
	prev := ListNode{Next: head}
	slow, fast := &prev, &prev
	twins := []int{}
	for fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		twins = append(twins, slow.Val)
	}
	slow = slow.Next
	twin := len(twins) - 1
	maxSum := 0
	for slow != nil {
		currSum := slow.Val + twins[twin]
		if currSum > maxSum {
			maxSum = currSum
		}
		twin--
		slow = slow.Next
	}
	return maxSum
}
