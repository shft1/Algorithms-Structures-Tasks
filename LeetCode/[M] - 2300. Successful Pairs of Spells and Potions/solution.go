package main

import "sort"

func successfulPairs(spells []int, potions []int, success int64) []int {
	sort.Ints(potions)
	for i := 0; i < len(spells); i++ {
		idx := searchLeft(potions, success, func(x int) int64 {
			return int64(x * spells[i])
		})
		if idx == len(potions) {
			spells[i] = 0
		} else {
			spells[i] = len(potions) - idx
		}
	}
	return spells
}

func searchLeft(arr []int, num int64, fn func(x int) int64) int {
	res := len(arr)
	left, right := 0, len(arr)-1
	for left <= right {
		mid := left + (right-left)/2
		if fn(arr[mid]) >= num {
			res = mid
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return res
}
