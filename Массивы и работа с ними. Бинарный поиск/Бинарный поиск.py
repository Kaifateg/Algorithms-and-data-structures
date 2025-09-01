import timeit
import matplotlib.pyplot as plt
import numpy as np


def search_binary(some_list, target):
    first = 0
    last = len(some_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if some_list[mid] == target:
            return mid
        elif some_list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1


def search_somthing(some_list, target):
    for index in range(len(some_list)):
        if int(some_list[index]) == int(target):
            return index
    return -1


random_list = np.random.randint(0, 100, size=100)
random_list.sort()
list_100 = list()
count0 = 0
while count0 != 10:
    random_numb = np.random.randint(1, 10)
    add_numb = search_binary(random_list, random_numb)
    list_100.append(add_numb)
    count0 += 1
print(list_100)


random_list_10 = np.random.randint(0, 100, size=10)
random_list_10.sort()
random_list_100 = np.random.randint(0, 100, size=100)
random_list_100.sort()
random_list_1000 = np.random.randint(0, 100, size=1000)
random_list_1000.sort()
rnd_numb = np.random.randint(1, 10)


test_code_linear_10 = """def test_time():
    search_somthing(random_list_10, rnd_numb)
"""
test_code_linear_100 = """def test_time():
    search_somthing(random_list_100, rnd_numb)
"""
test_code_linear_1000 = """def test_time():
    search_somthing(random_list_1000, rnd_numb)
"""
test_code_binary_10 = """def test_time():
    search_binary(random_list_10, rnd_numb)
"""
test_code_binary_100 = """def test_time():
    search_binary(random_list_100, rnd_numb)
"""
test_code_binary_1000 = """def test_time():
    search_binary(random_list_1000, rnd_numb)
"""


def fastest(rnd_list):
    numb = np.random.randint(1, 10)
    binary = timeit.timeit(stmt=test_code_binary_100, number=1000)
    linear = timeit.timeit(stmt=test_code_linear_100, number=1000)
    if binary > linear:
        print("Линейный поиск быстрее")
    else:
        print("Бинарный поиск быстрее")


fastest(random_list)


def append_list(test_code):
    times = []
    count = 0
    while count != 20:
        some_time = timeit.timeit(stmt=test_code, number=1000)
        times.append(float(some_time))
        count += 1
    return times


linear_list = append_list(test_code_linear_10) + append_list(
    test_code_linear_100) + append_list(test_code_linear_1000)

binary_list = append_list(test_code_binary_10) + append_list(
    test_code_binary_100) + append_list(test_code_binary_1000)


x = np.linspace(0, 60, 60)
y1 = linear_list
y2 = binary_list
plt.title("Зависимость времени от длины списка (от 10 до 1000)")
plt.xlabel("Количество измерений")
plt.ylabel("Время выполнения c увеличением длины списка")
plt.grid()
plt.plot(x, y1, label="Линейный поиск", color="red")
plt.plot(x, y2, label="Бинарный поиск", color="blue")
plt.legend()
plt.show()
