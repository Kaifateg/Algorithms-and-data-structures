class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return

    def resize(self):
        old_table = self.table.copy()
        old_len = len(self.table)
        new_len = 2 * old_len
        self.size = new_len
        self.table = [[] for _ in range(new_len)]
        for new_value in old_table:
            if len(new_value) != 0:
                index = self.hash_function(new_value[0][0])
                self.table[index] = new_value


a = HashTable(5)
print(a.table)
a.insert("top", 2)
a.insert("man", 5)
a.insert("dog", 10)
a.insert("Alise", "good")
print(a.search("man"))
a.resize()
a.delete("dog")
print(a.table)


def hash_func(strint):
    hash_list = [ord(value) for value in str(strint)]
    return sum(hash_list)


print(hash_func("brsfsfa!d"))


class Dictionary:
    def __init__(self):
        self.dictionary = dict()

    def add_value(self, value):
        self.dictionary[value] = hash_func(value)

    def search(self, value):
        if len(self.dictionary) > 0:
            return self.dictionary[value]
        else:
            return f"No dict"


dict1 = Dictionary()
dict1.add_value("Cake")
dict1.add_value("Potato")
dict1.add_value("Carrot")
dict1.add_value("Egg")
print(dict1.dictionary)
print(dict1.search("Potato"))
