class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.arr = [0] * capacity
        

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.len == self.capacity:
            self.resize()
        
        self.arr[self.len] = n
        self.len += 1

    def popback(self) -> int:
        self.len -= 1
        return self.arr[self.len]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity
        for i in range(self.len):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.len 
    
    def getCapacity(self) -> int:
        return self.capacity