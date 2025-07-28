def sift_down(heap, idx) -> int:
    left_idx = idx * 2
    if left_idx > len(heap) - 1:
        return idx
    if left_idx < len(heap) - 1 and heap[left_idx + 1] > heap[left_idx]:
        max_sibling_idx = left_idx + 1
    else:
        max_sibling_idx = left_idx
    if heap[idx] < heap[max_sibling_idx]:
        heap[idx], heap[max_sibling_idx] = heap[max_sibling_idx], heap[idx]
        return sift_down(heap, max_sibling_idx)
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == "__main__":
    test()
