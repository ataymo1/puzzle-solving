class Logger:

    def __init__(self):
        self.next_time = 0
        self.lookup = defaultdict(int)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.lookup[message] > timestamp:
                return False
        self.lookup[message] = timestamp + 10
        return True

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
