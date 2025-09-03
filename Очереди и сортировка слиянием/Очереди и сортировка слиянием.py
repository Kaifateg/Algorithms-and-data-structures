import time
import timeit
import matplotlib.pyplot as plt
import numpy as np
import datetime
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")


targets = Queue()
targets.enqueue("Работа")
targets.enqueue("Стирка")
targets.enqueue("Уборка")
targets.enqueue("Готовка")

while not targets.is_empty():
    target_time = datetime.datetime.now()
    if targets.peek() == "Работа":
        time.sleep(3)
        print(f"Цель {targets.peek()} выполнена в"
              f" {target_time.strftime('%H:%M:%S')}")
        targets.dequeue()
    elif targets.peek() == "Готовка":
        time.sleep(2)
        print(f"Цель {targets.peek()} выполнена в "
              f"{target_time.strftime('%H:%M:%S')}")
        targets.dequeue()
    else:
        time.sleep(5)
        print(f"Цель {targets.peek()} выполнена в "
              f"{target_time.strftime('%H:%M:%S')}")
        targets.dequeue()


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


test_list = [7, 0, 44, 33, 2, 41]
print(merge_sort(test_list))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


random_list_10 = np.random.randint(0, 100, size=10)
random_list_100 = np.random.randint(0, 100, size=100)
random_list_1000 = np.random.randint(0, 100, size=1000)

test_code_bubble_10 = """def test_time():
    bubble_sort(random_list_10)
"""
test_code_bubble_100 = """def test_time():
    bubble_sort(random_list_100)
"""
test_code_bubble_1000 = """def test_time():
    bubble_sort(random_list_1000)
"""
test_code_merge_10 = """def test_time():
    insertion_sort(random_list_10)
"""
test_code_merge_100 = """def test_time():
    insertion_sort(random_list_100)
"""
test_code_merge_1000 = """def test_time():
    insertion_sort(random_list_1000)
"""


def append_list(test_code):
    times = []
    count = 0
    while count != 20:
        some_time = timeit.timeit(stmt=test_code, number=1000)
        times.append(float(some_time))
        count += 1
    return times


bubble_list = append_list(test_code_bubble_10) + append_list(
    test_code_bubble_100) + append_list(test_code_bubble_1000)

merge_list = append_list(test_code_merge_10) + append_list(
    test_code_merge_100) + append_list(test_code_merge_1000)


x = np.linspace(0, 60, 60)
y1 = bubble_list
y2 = merge_list

plt.title("Зависимость времени от длины списка (от 10 до 1000)")
plt.xlabel("Количество измерений")
plt.ylabel("Время выполнения c увеличением длины списка")
plt.grid()
plt.plot(x, y1, label="Сортировка слиянием", color="red")
plt.plot(x, y2, label="Сортировка пузырьком", color="blue")
plt.legend()
plt.show()
