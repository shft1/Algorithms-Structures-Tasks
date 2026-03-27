package main

func intersection(nums1 []int, nums2 []int) []int {
	m1, m2 := make(map[int]struct{}), make(map[int]struct{})
	for _, n1 := range nums1 {
		m1[n1] = struct{}{}
	}
	for _, n2 := range nums2 {
		m2[n2] = struct{}{}
	}
	var res []int
	for k := range m1 {
		if _, ok := m2[k]; ok {
			res = append(res, k)
		}
	}
	return res
}
