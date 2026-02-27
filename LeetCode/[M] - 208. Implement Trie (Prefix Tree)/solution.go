package main

type Trie struct {
	isWord    bool
	childrens map[rune]*Trie
}

func Constructor() Trie {
	return Trie{childrens: make(map[rune]*Trie)}
}

func (t *Trie) Insert(word string) {
	for _, char := range word {
		if _, ok := t.childrens[char]; !ok {
			t.childrens[char] = &Trie{childrens: make(map[rune]*Trie)}
		}
		t = t.childrens[char]
	}
	t.isWord = true
}

func (t *Trie) Search(word string) bool {
	for _, char := range word {
		if _, ok := t.childrens[char]; !ok {
			return false
		}
		t = t.childrens[char]
	}
	return t.isWord
}

func (t *Trie) StartsWith(prefix string) bool {
	for _, char := range prefix {
		if _, ok := t.childrens[char]; !ok {
			return false
		}
		t = t.childrens[char]
	}
	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
