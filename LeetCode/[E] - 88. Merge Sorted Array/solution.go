package main

func merge(nums1 []int, m int, nums2 []int, n int) {
	ins, l, r := n+m-1, m-1, n-1
	for r >= 0 {
		if l >= 0 && nums1[l] > nums2[r] {
			nums1[ins] = nums1[l]
			l--
		} else {
			nums1[ins] = nums2[r]
			r--
		}
		ins--
	}
}
