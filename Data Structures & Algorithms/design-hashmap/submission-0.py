class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        for i in self.hashMap:
            if key == i[0]:
                i[1] = value
                return
        self.hashMap.append([key,value])
            
                

    def get(self, key: int) -> int:
        for i in self.hashMap:
            if key == i[0]:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.hashMap:
            if key == i[0]:
                self.hashMap.remove(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)