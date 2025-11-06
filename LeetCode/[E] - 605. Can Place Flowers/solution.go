package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	newFlowered := make([]int, 0, len(flowerbed)+2)
	newFlowered = append(newFlowered, 0)
	newFlowered = append(newFlowered, flowerbed...)
	newFlowered = append(newFlowered, 0)
	for i := 1; i != len(newFlowered)-1; i++ {
		if newFlowered[i-1] != 1 && newFlowered[i] != 1 && newFlowered[i+1] != 1 {
			newFlowered[i] = 1
			n--
		}
	}
	if n <= 0 {
		return true
	} else {
		return false
	}
}
