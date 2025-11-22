package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	mapNum1 := make(map[int]struct{})
	mapNum2 := make(map[int]struct{})
	for _, el := range nums1 {
		mapNum1[el] = struct{}{}
	}
	for _, el := range nums2 {
		mapNum2[el] = struct{}{}
	}
	res := make([][]int, 2)
	for key := range mapNum1 {
		if _, ok := mapNum2[key]; !ok {
			res[0] = append(res[0], key)
		}
	}
	for key := range mapNum2 {
		if _, ok := mapNum1[key]; !ok {
			res[1] = append(res[1], key)
		}
	}
	return res
}
