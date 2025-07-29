"""
ID посылки - https://contest.yandex.ru/contest/24810/run-report/140560899/

Задача: Реализовать пирамидальную сортировку (сортировку кучей)

Примечание:
Куча реализована на массиве, хотя удобно представлять ее как бинарное дерево, где 1 номер ячейки - самый приоритетный элемент кучи.
Левый потомок вершины - i * 2
Правый потомок вершины - i * 2 + 1
Родитель вершины - i // 2

Для каждой операции, которая изменяет кучу, должен запускаться алгоритм восставновления свойств кучи:
1. Просеивание вверх - алгоритм восстановления свойств кучи при добавлении нового элемента.
2. Просеивание вниз - алгоритм восстановления свойств кучи при удалении самого приоритетного элемента.

--- Принцип работы ---
Для данной задачи строится MinHeap куча
1. Создание кучи
Каждый поступающий на вход элемент добавляется в кучу.
Для каждой операции добавления, кроме первой, запускается процедура просеивания вверх, чтобы соответствовать св-вам кучи
2. Поочередное извлечение самого приоритетного элемента кучи (элемента с i=1 / вершина кучи)
Для каждой операции извлечения, кроме последней, запускается процедура просеивания вниз, чтобы соответствовать св-вам кучи
3. Каждый извлеченный элемент из кучи добавляется в массив
4. Полученный массив является отсортированным в соответствии с построением кучи, MinHeap - по возрастанию

--- Доказательства корректности ---
Благодаря тому, что на вершине кучи поддерживается самый приоритетный элемент, массив получается отсортированным.

--- Временная сложность ---
Временная сложность алгоритма пирамидальной сортировки (не in-place) складывается из сложностей:
1. Создание массива фиксированной длины -> O(1)
2. Заполнение кучи из n элементов -> O(nlogn)
Для каждой операции добавления вызывается алгоритм просеивания вверх, поскольку, по св-ву кучи,
дерево у нас почти полное, это значит, что в худшем случае нам придется пройти все logN уровней, следовательно,
сложность создания кучи из n элементов равна O(nlogn)
3. Извлечение из кучи n элементов -> O(nlogn)
Для каждой операции извлечения вызывается алгоритм просеивания вниз, поскольку, по св-ву кучи,
дерево у нас почти полное, это значит, что в худшем случае нам придется пройти все logN уровней, следовательно,
сложность извлечения из кучи n элементов равна O(nlogn)
4. Добавление извлеченных элементов из кучи в новый, результирующий массив - O(n)
---> Итоговая временная сложность - O(1 + nlogn + nlogn + n) = O(nlogn)

--- Пространственная сложность ---
Пространственная сложность алгоритма пирамидальной сортировки (не in-place) складывается из сложностей:
1. Выделение памяти под кучу размером n -> O(n)
2. Выделение памяти под результирующий массив отсортированных n элементов -> O(n)
---> Итоговая пространственная сложность - O(n + n) = O(n)
"""

import sys


class MinHeap:
    def __init__(self, size, func_key=lambda x: x) -> None:
        self.size = size
        self.last_idx = 0
        self.func_key = func_key
        self.heap = [None] * (self.size + 1)

    def _sift_up(self, idx: int) -> None:
        if idx == 1:
            return
        p_idx = idx // 2
        if self.func_key(self.heap[idx]) < self.func_key(self.heap[p_idx]):
            self.heap[p_idx], self.heap[idx] = self.heap[idx], self.heap[p_idx]
            self._sift_up(p_idx)

    def add(self, obj) -> None:
        if self.last_idx == self.size:
            raise RuntimeError("Куча переполнена!")
        self.last_idx += 1
        self.heap[self.last_idx] = obj
        self._sift_up(self.last_idx)

    def _sift_down(self, idx: int) -> None:
        l_idx = idx * 2
        if l_idx > self.last_idx:
            return
        if l_idx < self.last_idx and self.func_key(
            self.heap[l_idx + 1]
        ) < self.func_key(self.heap[l_idx]):
            min_idx = l_idx + 1
        else:
            min_idx = l_idx
        if self.func_key(self.heap[min_idx]) < self.func_key(self.heap[idx]):
            self.heap[min_idx], self.heap[idx] = (
                self.heap[idx],
                self.heap[min_idx],
            )
            self._sift_down(min_idx)

    def pop_max(self) -> list[str]:
        if self.last_idx == 0:
            raise RuntimeError("Куча пуста!")
        max_obj = self.heap[1]
        self.heap[1] = self.heap[self.last_idx]
        self.heap[self.last_idx] = None
        self.last_idx -= 1
        self._sift_down(1)
        return max_obj


def func_key(obj) -> tuple:
    return (-int(obj[1]), int(obj[2]), obj[0])


def heap_sort(n: int) -> list[str]:
    heap = MinHeap(size=n, func_key=func_key)
    try:
        for _ in range(n):
            obj = sys.stdin.readline().rstrip().split()
            heap.add(obj)
        return [heap.pop_max()[0] for _ in range(n)]
    except RuntimeError as e:
        return f"Ошибка-при-работе-с-кучей--->{e}"


def main():
    n: int = int(sys.stdin.readline().rstrip())
    res: list[str] = heap_sort(n)
    sys.stdout.write("\n".join(res))


if __name__ == "__main__":
    main()
