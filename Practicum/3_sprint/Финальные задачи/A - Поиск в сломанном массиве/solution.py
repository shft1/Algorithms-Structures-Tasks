# -- Решение без поиска сдвига --
def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] <= nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 7, 12, 19, 21, 100, 101, 1, 4]
    assert broken_search(arr, 5) == 0
    arr = [5, 1]
    assert broken_search(arr, 1) == 1


# -- Решение с поиском сдвига --
# def find_shift(nums) -> int:
#     shift: int = 0
#     i: int = 0
#     for num in nums:
#         if num < nums[shift]:
#             shift = i
#         i += 1
#     return shift, i


# def broken_search(nums, target) -> int:
#     shft, n = find_shift(nums)
#     left: int = 0
#     right: int = n - 1
#     while left <= right:
#         mid: int = (left + right) // 2
#         mid_shft: int = (mid + shft) % n
#         if target == nums[mid_shft]:
#             return mid_shft
#         elif target < nums[mid_shft]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1


# def test():
#     arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
#     assert broken_search(arr, 5) == 6
#     arr = [5, 7, 12, 19, 21, 100, 101, 1, 4]
#     assert broken_search(arr, 5) == 0
