package main

import "slices"

func suggestedProducts(products []string, searchWord string) [][]string {
	slices.Sort(products)

	searchSystem := make(map[string][]string)

	for _, product := range products {
		for i := range product {
			key := product[:i+1]
			searchSystem[key] = append(searchSystem[key], product)
		}
	}

	res := make([][]string, len(searchWord))
	for i := range searchWord {
		key := searchWord[:i+1]
		if _, ok := searchSystem[key]; !ok {
			return res
		}
		if len(searchSystem[key]) > 3 {
			searchSystem[key] = searchSystem[key][:3]
		}
		res[i] = searchSystem[key]
	}
	return res
}
