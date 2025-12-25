package main

// TreeNode - Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	res := make([]int, 0, 100)
	queue := make([]*TreeNode, 0, 100)
	queue = append(queue, root)
	for len(queue) != 0 {
		res = append(res, queue[len(queue)-1].Val)
		lenQ := len(queue)
		for i := 1; i <= lenQ; i++ {
			v := queue[0]
			queue = queue[1:]
			if v.Left != nil {
				queue = append(queue, v.Left)
			}
			if v.Right != nil {
				queue = append(queue, v.Right)
			}
		}
	}
	return res
}
