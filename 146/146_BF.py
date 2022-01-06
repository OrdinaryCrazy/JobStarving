class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_val_times = []

    def get(self, key: int) -> int:
        out = -1
        for i, kvt in enumerate(self.key_val_times):
            key_l, val, times = kvt
            if key_l == key:
                out = val
                self.key_val_times[i] = (key_l, val, 0)
            else:
                self.key_val_times[i] = (key_l, val, times + 1)
        # print(self.key_val_times)
        return out

    def put(self, key: int, value: int) -> None:
        if len(self.key_val_times) == self.cap:
            max_t = -float('inf')
            max_i = 0
            for i, kvt in enumerate(self.key_val_times):
                k, v, t = kvt
                if k == key:
                    self.key_val_times[i] = (key, value, 0)
                    max_t = -1
                else:
                    if t > max_t and max_t != -1:
                        max_t = t
                        max_i = i
                    self.key_val_times[i] = (k, v, t + 1)
            if max_t != -1:
                self.key_val_times[max_i] = (key, value, 0)
        else:
            found = -1
            for i, kvt in enumerate(self.key_val_times):
                k, v, t = kvt
                if k == key:
                    self.key_val_times[i] = (key, value, 0)
                    found = 1
                else:
                    self.key_val_times[i] = (k, v, t + 1)
            if found == -1:
                self.key_val_times.append((key, value, 0))
        # print(self.key_val_times)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)