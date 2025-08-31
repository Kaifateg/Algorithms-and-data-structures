import random
import timeit
import matplotlib.pyplot as plt
import numpy as np


def search_somthing(some_list, element):
    for index in range(len(some_list)):
        if int(some_list[index]) == int(element):
            return index
    return -1


random_list = [random.randint(1, 100) for _ in range(100)]
list_100 = list()
count0 = 0
while count0 != 10:
    random_numb = random.randint(1, 10)
    add_numb = search_somthing(random_list, random_numb)
    list_100.append(add_numb)
    count0 += 1
print(list_100)


test_code_10 = """def test_time():
    random_list = [random.randint(1, 100) for _ in range(10)]
    random_numb = random.randint(1, 10)
    print(search_somthing(random_list, random_numb))
"""
test_code_100 = """def test_time():
    random_list = [random.randint(1, 100) for _ in range(100)]
    random_numb = random.randint(1, 10)
    print(search_somthing(random_list, random_numb))
"""
test_code_1000 = """def test_time():
    random_list = [random.randint(1, 100) for _ in range(1000)]
    random_numb = random.randint(1, 10)
    print(search_somthing(random_list, random_numb))
"""


times_10 = []
times_100 = []
times_1000 = []
count = 0

while count != 50:
    some_time_10 = timeit.timeit(stmt=test_code_10, number=1000)
    some_time_100 = timeit.timeit(stmt=test_code_100, number=1000)
    some_time_1000 = timeit.timeit(stmt=test_code_1000, number=1000)
    times_10.append(float(some_time_10))
    times_100.append(float(some_time_100))
    times_1000.append(float(some_time_1000))
    count += 1


x = np.linspace(0, 50, 50)
y1 = times_10
y2 = times_100
y3 = times_1000
plt.title("Зависимость времени от длины списка")
plt.xlabel("Количество измерений")
plt.ylabel("Время выполнения")
plt.grid()
plt.plot(x, y1, label="Список из 10 элементов", color="green")
plt.plot(x, y2, label="Список из 100 элементов", color="blue")
plt.plot(x, y3, label="Список из 1000 элементов", color="red")
plt.legend()
plt.show()
