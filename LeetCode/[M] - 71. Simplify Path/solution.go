package main

import "strings"

func simplifyPath(path string) string {
	var stack []string
	for _, way := range strings.Split(path, "/") {
		if way != "." && way != "" && way != ".." {
			stack = append(stack, way)
		} else if way == ".." && len(stack) != 0 {
			stack = stack[:len(stack)-1]
		}
	}
	return "/" + strings.Join(stack, "/")
}
