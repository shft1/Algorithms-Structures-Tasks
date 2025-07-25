"""
ID посылки - https://contest.yandex.ru/contest/23815/run-report/139997812/

--- Принцип работы ---

Задача: обеспечить поиск элемента за O(logn) в сдвинутом массиве.

Алгоритм работает по принципу бинарного поиска, но с некоторым отличием:
Поскольку массив сдвинут, то нарушается порядок сортировки, а именно, мы не можем сказать,
что если искомое число меньше центрального, то оно обязательно в левой части, ведь в правой части только бОльшие,
в данном случае, в правой части могут быть тоже меньшие центрального, ведь сортировка нарушена.
Но можно заметить, что в любой момент времени, хотя бы одна из частей является отсортированной, именно по этой части
мы можем сказать, что если элемент лежит в ее границах, то работаем с ней, если нет, то работаем с другой.

Заводим два указателя (left/right), изначально указывающие на начало и конец массива соответственно.
1. Вычисляем середину (mid).
2. Находим, какая из частей является отсортированной
3. Проверяем, лежит ли искомый элемент в границах части
4. Если лежит, то работам с ней, если нет, работам с другой
5. Возвращаемся в 1 пункт.

--- Доказательства корректности ---

Скорость бинарного поиска достигается за счет того, что на каждом шаге отбрасывается половина массива,
в котором этот элемент точно не может быть. Данный алгоритм сохраняет скорость бинарного поиска, за счет того,
что в любой момент времени у нас есть хотя бы одна отсортированная часть, благодаря которой, мы можем проверить
принадлежность элемента к этой, отсортированной части и, в зависимости от результата, отбросить одну из половин.

--- Временная сложность ---

Данный алгоритм работает за O(logn), тк на каждом шаге отбрасывается половина массива.
Итоговая временная сложность - O(logn)

--- Пространственная сложность ---

Данный алгоритм не потребляет дополнительную память, поэтому его пространственная сложность равна O(1)
Итоговая временная сложность - O(1)
"""


def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
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
