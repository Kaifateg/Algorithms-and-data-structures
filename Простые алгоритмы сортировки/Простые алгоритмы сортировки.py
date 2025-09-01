import timeit
import matplotlib.pyplot as plt
import numpy as np


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


random_list_100 = np.random.randint(0, 100, size=100)
random_list_1000 = np.random.randint(0, 100, size=1000)
random_list_10000 = np.random.randint(0, 100, size=10000)

test_code_bubble_100 = """def test_time():
    bubble_sort(random_list_100)
"""
test_code_bubble_1000 = """def test_time():
    bubble_sort(random_list_1000)
"""
test_code_bubble_10000 = """def test_time():
    bubble_sort(random_list_10000)
"""
test_code_selection_100 = """def test_time():
    selection_sort(random_list_100)
"""
test_code_selection_1000 = """def test_time():
    selection_sort(random_list_1000)
"""
test_code_selection_10000 = """def test_time():
    selection_sort(random_list_10000)
"""
test_code_insertion_100 = """def test_time():
    insertion_sort(random_list_100)
"""
test_code_insertion_1000 = """def test_time():
    insertion_sort(random_list_1000)
"""
test_code_insertion_10000 = """def test_time():
    insertion_sort(random_list_10000)
"""


def fastest():
    bubble = timeit.timeit(stmt=test_code_bubble_100, number=1000)
    selection = timeit.timeit(stmt=test_code_insertion_100, number=1000)
    insertion = timeit.timeit(stmt=test_code_selection_100, number=1000)
    if bubble < selection and bubble < insertion:
        print("Сортировка пузырьком быстрее")
    elif selection < bubble and selection < insertion:
        print("Сортировка выбором быстрее")
    elif insertion < bubble and insertion < selection:
        print("Сортировка вставками быстрее")
    else:
        print("Не всё так однозначно")


fastest()


def append_list(test_code):
    times = []
    count = 0
    while count != 20:
        some_time = timeit.timeit(stmt=test_code, number=1000)
        times.append(float(some_time))
        count += 1
    return times


bubble_list = append_list(test_code_bubble_100) + append_list(
    test_code_bubble_1000) + append_list(test_code_bubble_10000)

selection_list = append_list(test_code_selection_100) + append_list(
    test_code_selection_1000) + append_list(test_code_selection_10000)

insertion_list = append_list(test_code_insertion_100) + append_list(
    test_code_insertion_1000) + append_list(test_code_insertion_10000)

x = np.linspace(0, 60, 60)
y1 = bubble_list
y2 = selection_list
y3 = insertion_list
plt.title("Зависимость времени от длины списка (от 100 до 10000)")
plt.xlabel("Количество измерений")
plt.ylabel("Время выполнения c увеличением длины списка")
plt.grid()
plt.plot(x, y1, label="Сортировка пузырьком", color="red")
plt.plot(x, y2, label="Сортировка выбором", color="blue")
plt.plot(x, y3, label="Сортировка вставками", color="green")
plt.legend()
plt.show()
