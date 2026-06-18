class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.arr = [0] * size
        self.reached = False
        self.total = 0
        self.index = 0

        

    def next(self, val: int) -> float:
        if not self.reached:
            if self.index == self.size:
                self.index = 0
                self.reached = True
                self.total -= self.arr[self.index]
                self.arr[self.index] = val
                self.total += self.arr[self.index]
                self.index += 1
                # print(self.arr)
                return self.total / self.size
            self.arr[self.index] = val
            self.total += self.arr[self.index]
            self.index += 1
            # print(self.arr)
            return self.total / self.index
        
        self.total -= self.arr[self.index]
        self.arr[self.index] = val
        self.total += self.arr[self.index]
        self.index = (self.index + 1) % self.size
        # print(self.arr)
        return self.total / self.size

            
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
