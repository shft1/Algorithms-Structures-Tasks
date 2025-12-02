package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 1<<20)

	nums := make([]int, 0, 10)
	for i := 0; i < 10; i++ {
		line, _ := reader.ReadString('\n')
		num, _ := strconv.Atoi(strings.Fields(line)[0])
		nums = append(nums, num)
	}

	sums := make([]int, 1, 1024)
	for _, num := range nums {
		currSum := make([]int, 100)
		for _, sum := range sums {
			currSum = append(currSum, sum+num)
		}
		sums = append(sums, currSum...)
	}
	diff := 101
	res := -1
	for _, sum := range sums {
		currDiff := 0
		if 100-sum > 0 {
			currDiff = 100 - sum
		} else {
			currDiff = (100 - sum) * -1
		}
		if currDiff == 0 {
			diff = currDiff
			res = sum
		} else if currDiff < diff {
			diff = currDiff
			res = sum
		} else if currDiff == diff && sum > res {
			diff = currDiff
			res = sum
		}
	}
	fmt.Printf("%d\n", res)
}
