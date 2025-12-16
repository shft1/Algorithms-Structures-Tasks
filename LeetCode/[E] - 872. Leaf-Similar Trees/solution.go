package main

import "slices"

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	leafes1, leafes2 := make([]int, 0, 100), make([]int, 0, 100)
	leafesCollect(root1, &leafes1)
	leafesCollect(root2, &leafes2)
	return slices.Equal(leafes1, leafes2)
}

func leafesCollect(node *TreeNode, leafes *[]int) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		*leafes = append(*leafes, node.Val)
		return
	}
	leafesCollect(node.Left, leafes)
	leafesCollect(node.Right, leafes)
}
