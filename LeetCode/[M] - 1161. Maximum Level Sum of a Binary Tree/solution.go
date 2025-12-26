package main

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxLevelSum(root *TreeNode) int {
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	maxSum := root.Val
	level, currLevel := 1, 0
	for len(queue) != 0 {
		currLevel++
		currSum := 0
		lenQ := len(queue)
		for i := 0; i < lenQ; i++ {
			v := queue[0]
			queue = queue[1:]
			currSum += v.Val
			if v.Left != nil {
				queue = append(queue, v.Left)
			}
			if v.Right != nil {
				queue = append(queue, v.Right)
			}
		}
		if currSum > maxSum {
			maxSum = currSum
			level = currLevel
		}
	}
	return level
}
