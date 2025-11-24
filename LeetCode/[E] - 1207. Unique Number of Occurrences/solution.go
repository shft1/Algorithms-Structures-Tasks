package main

func uniqueOccurrences(arr []int) bool {
	symbCount := make(map[int]int, len(arr)/2)
	for _, el := range arr {
		symbCount[el] += 1
	}
	countSet := make(map[int]struct{}, len(symbCount))
	for _, value := range symbCount {
		if _, ok := countSet[value]; ok {
			return false
		}
		countSet[value] = struct{}{}
	}
	return true
}
