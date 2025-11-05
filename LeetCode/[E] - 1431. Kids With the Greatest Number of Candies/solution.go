package main

func kidsWithCandies(candies []int, extraCandies int) []bool {
	var maxCand int
	for _, el := range candies {
		if el > maxCand {
			maxCand = el
		}
	}
	res := make([]bool, 0, len(candies))
	for _, el := range candies {
		if el+extraCandies >= maxCand {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}
	return res
}
