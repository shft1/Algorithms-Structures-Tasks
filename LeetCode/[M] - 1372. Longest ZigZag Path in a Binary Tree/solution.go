package main

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func longestZigZag(root *TreeNode) int {
	var res int
	searchZigZag(root.Right, 'l', 1, &res)
	searchZigZag(root.Left, 'r', 1, &res)
	return res
}

func searchZigZag(node *TreeNode, direction byte, curr int, res *int) {
	if node == nil {
		return
	}
	if direction == 'r' {
		searchZigZag(node.Right, 'l', curr+1, res)
		searchZigZag(node.Left, 'r', 1, res)
	} else if direction == 'l' {
		searchZigZag(node.Left, 'r', curr+1, res)
		searchZigZag(node.Right, 'l', 1, res)
	}
	*res = max(*res, curr)
}
