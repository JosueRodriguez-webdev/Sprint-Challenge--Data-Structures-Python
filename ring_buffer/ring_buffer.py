
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.arr = []

    def append(self, item):
        if item is None:
            return
        if len(self.arr) == self.capacity:
            if self.length == self.capacity:
                self.length = 0
            else:
                self.arr[self.length] = item
                self.length += 1
        if len(self.arr) < self.capacity:
            self.arr.append(item)

    def get(self):
        return self.arr
