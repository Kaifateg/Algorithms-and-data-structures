from random import randint


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))


def list_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[-1] + list_sum(arr[:-1])


print(list_sum([1, 2, 3, 4, 5]))


def binary_funk(arr, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_funk(arr, low, mid-1, target)
        else:
            return binary_funk(arr, mid+1, high, target)
    else:
        return -1


rnd_list = [randint(0, 10) for _ in range(10)]
rnd_list.sort()
print(binary_funk(rnd_list, 0, len(rnd_list), 7))


class Stack:
    def __init__(self):
        self.create_list = []

    def is_empty(self):
        return len(self.create_list) == 0

    def push(self, value):
        self.create_list.append(value)

    def pop(self):
        if not self.is_empty():
            return self.create_list.pop()
        else:
            print("Список пуст")

    def peek(self):
        if not self.is_empty():
            return self.create_list[-1]
        else:
            print("Список пуст")


test = Stack()
test.push(5)
test.push("low")
test.push(15)
print(test.pop())
print(test.peek())
print(test.is_empty())
