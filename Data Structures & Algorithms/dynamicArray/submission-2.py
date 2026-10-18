class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise Error('Capacity must be greater than zero')
        self.capacity = capacity
        self.size = -1
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        if i > self.size:
            raise IndexError(f'Index {i} out of range')
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        if i > self.size:
            raise IndexError(f'Index {i} out of range')
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.size + 1 >= self.capacity:
            self.resize()

        self.size += 1
        self.arr[self.size] = n


    def popback(self) -> int:
        val = self.arr[self.size]
        self.size -= 1
        return val
 

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] *  self.capacity
        for i in range(self.size + 1):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size + 1
        
    
    def getCapacity(self) -> int:
        return self.capacity
