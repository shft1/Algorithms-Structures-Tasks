package main

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goodNodes(root *TreeNode) int {
	var cnt int
	searchGoodNodes(root.Val, root, &cnt)
	return cnt
}

func searchGoodNodes(maxVal int, node *TreeNode, cnt *int) {
	if node == nil {
		return
	}
	if node.Val >= maxVal {
		*cnt += 1
		maxVal = node.Val
	}
	searchGoodNodes(maxVal, node.Left, cnt)
	searchGoodNodes(maxVal, node.Right, cnt)
}
