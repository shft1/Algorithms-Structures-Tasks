package main

import "math"

// TreeNode Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	var fn func(*TreeNode, int, int) bool
	fn = func(root *TreeNode, left, right int) bool {
		if root == nil {
			return true
		}
		if root.Val <= left || root.Val >= right {
			return false
		}
		return fn(root.Left, left, root.Val) && fn(root.Right, root.Val, right)
	}
	return fn(root, math.MinInt64, math.MaxInt64)
}
