import timeit
import matplotlib.pyplot as plt
import numpy as np


# Стек вызовов для числа 5 составляет - 15 (из-за повторяющихся вызовов)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


def merge_sort(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        return max(merge_sort(left_half), merge_sort(right_half))


print(merge_sort([9, 100, 5, 6, 6, 8, 0, 8, 33]))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = []
        right = []
        middle = []
        for i in arr:
            if i > pivot:
                right.append(i)
            elif i < pivot:
                left.append(i)
            else:
                middle.append(i)
        return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([100, 0, 33, 100, 3, 2, 0]))


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


random_list_10 = np.random.randint(0, 100, size=10)
random_list_100 = np.random.randint(0, 100, size=100)
random_list_1000 = np.random.randint(0, 100, size=1000)

test_code_quick_10 = """def test_time():
    quick_sort(random_list_10)
"""
test_code_quick_100 = """def test_time():
    quick_sort(random_list_100)
"""
test_code_quick_1000 = """def test_time():
    quick_sort(random_list_1000)
"""
test_code_selection_10 = """def test_time():
    selection_sort(random_list_10)
"""
test_code_selection_100 = """def test_time():
    selection_sort(random_list_100)
"""
test_code_selection_1000 = """def test_time():
    selection_sort(random_list_1000)
"""


def append_list(test_code):
    times = []
    count = 0
    while count != 20:
        some_time = timeit.timeit(stmt=test_code, number=1000)
        times.append(float(some_time))
        count += 1
    return times


quick_list = append_list(test_code_quick_10) + append_list(
    test_code_quick_100) + append_list(test_code_quick_1000)

selection_list = append_list(test_code_selection_10) + append_list(
    test_code_selection_100) + append_list(test_code_selection_1000)


x = np.linspace(0, 60, 60)
y1 = quick_list
y2 = selection_list
plt.title("Зависимость времени от длины списка (от 10 до 1000)")
plt.xlabel("Количество измерений")
plt.ylabel("Время выполнения c увеличением длины списка")
plt.grid()
plt.plot(x, y1, label="Быстрая сортировка", color="red")
plt.plot(x, y2, label="Сортировка выбором", color="blue")
plt.legend()
plt.show()
