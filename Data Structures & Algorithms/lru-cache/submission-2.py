from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.queue = deque()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.items:
            self.items[key] = tuple((self.items[key][0], self.items[key][1] + 1))
            self.queue.append(tuple((key, self.items[key])))
            return self.items[key][0]
        return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.items:
            self.items[key] = tuple((value, self.items[key][1] + 1))
            self.queue.append(tuple((key, self.items[key])))
            return

        amount = len(self.items.keys())
        
        while self.queue and amount >= self.capacity:
            popped_key, popped_cache = self.queue.popleft()
            if popped_cache == self.items[popped_key]:
                self.items.pop(popped_key)
                break
        
        self.items[key] = tuple((value, 0))
        self.queue.append(tuple((key, self.items[key])))



            

        



        

        
