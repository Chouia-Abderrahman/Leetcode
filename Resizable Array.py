class DynamicArray:

    def __init__(self, capacity: int):
        # DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def get(self, i: int) -> int:
        # int get(int i) will return the element at index i. Assume that index i is valid.
        return self.data[i]
        pass
    def set(self, i: int, n: int) -> None:
        #void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
        self.data[i] = n
        # pass
    def pushback(self, n: int) -> None:
        #void pushback(int n) will push the element n to the end of the array.
        if self.size == self.capacity:
            print("Can' pushback, array already full")
            return
        if self.size == 0:
            self.data[self.size] = n
        self.data[self.size] = n
        self.size += 1


    def popback(self) -> int:
        # int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.

        # return self.data[self.size - 1]
        return self.data.pop(self.size - 1)

    def resize(self) -> None:
        # void resize() will double the capacity of the array.
        new_data = [None] * self.capacity * 2
        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def getSize(self) -> int:
        # int getSize() will return the number of elements in the array.
        return self.size

    def getCapacity(self) -> int:
        # int getCapacity() will return the capacity of the array.
        return self.capacity