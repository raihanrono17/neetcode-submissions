class MyHashSet:

    def __init__(self):
        self.seen = []
        
    def add(self, key: int) -> None:
        if key not in self.seen:
            self.seen.append(key)
    def remove(self, key: int) -> None:
        if key in self.seen:
            self.seen.remove(key)

    def contains(self, key: int) -> bool:
        for i in range(len(self.seen)):
            if self.seen[i] == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)