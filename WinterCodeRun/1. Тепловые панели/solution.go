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

	line, _ := reader.ReadString('\n')
	parts := strings.Fields(line)

	R, _ := strconv.Atoi(parts[0])
	B, _ := strconv.Atoi(parts[1])

	sum := B + R
	d := 1
	for h := 2; h*h <= sum; h++ {
		if sum%h == 0 && ((h-2)*(sum/h-2)) == B {
			d = h
			break
		}
	}
	fmt.Printf("%d %d\n", sum/d, d)
}
