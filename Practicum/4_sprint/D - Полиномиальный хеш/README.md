D. Полиномиальный хеш

Все языки	Python 3.11.4

Ограничение времени	0.5 секунд	0.65 секунд

Ограничение памяти	64Mb	64Mb

Ввод	стандартный ввод или input.txt

Вывод	стандартный вывод или output.txt

Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей написать функцию, вычисляющую хеш строки s. 

В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:



Формат ввода

В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 109) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 106), состоящая из больших и маленьких латинских букв.

Формат вывода

Выведите целое неотрицательное число –— хеш заданной строки.

Пример 1

Ввод	Вывод

123

100003

a

97

Пример 2

Ввод	Вывод

123

100003

hash

6080

Пример 3

Ввод	Вывод

123

100003

HaSH

56156
