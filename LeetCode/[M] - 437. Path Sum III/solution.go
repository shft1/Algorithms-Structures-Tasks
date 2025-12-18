package main

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, targetSum int) int {
	freq := map[int]int{0: 1}
	res := 0

	var dfs func(node *TreeNode, ps int)
	dfs = func(node *TreeNode, ps int) {
		if node == nil {
			return
		}
		cs := ps + node.Val
		x := cs - targetSum

		res += freq[x]
		freq[cs] += 1

		dfs(node.Left, cs)
		dfs(node.Right, cs)

		freq[cs] -= 1
	}
	dfs(root, 0)
	return res
}
