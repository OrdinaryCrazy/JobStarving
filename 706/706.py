class MyHashMap:

    def __init__(self):
        self.size = 100
        self.keys = [[]] * self.size
        self.vals = [[]] * self.size

    def put(self, key: int, value: int) -> None:
        key_h = key % self.size
        if key in self.keys[key_h]:
            idx = self.keys[key_h].index(key)
            self.vals[key_h][idx] = value
        else:
            self.keys[key_h].append(key)
            self.vals[key_h].append(value)

    def get(self, key: int) -> int:
        key_h = key % self.size
        if key in self.keys[key_h]:
            idx = self.keys[key_h].index(key)
            return self.vals[key_h][idx]
        else:
            return -1

    def remove(self, key: int) -> None:
        key_h = key % self.size
        if key in self.keys[key_h]:
            idx = self.keys[key_h].index(key)
            self.vals[key_h].pop(idx)
            self.keys[key_h].pop(idx)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)