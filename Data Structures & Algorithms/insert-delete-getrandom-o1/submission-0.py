class RandomizedSet:

    def __init__(self):
        self.mp = {}
        self.values = []
        self.idx = 0

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.mp[val] = self.idx
        self.values.append(val)
        self.idx += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        self.idx -= 1
        pos = self.mp[val]
        self.values[pos], self.values[self.idx] = self.values[self.idx], self.values[pos]
        self.mp[self.values[pos]] = pos
        rm_value = self.values.pop()
        del self.mp[rm_value]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()