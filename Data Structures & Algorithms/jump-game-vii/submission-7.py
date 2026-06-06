from functools import cache
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        visited = set()
        if s[-1] != '0':
            return False

        length = len(s) - 1
        
        def jump(i):
            if i == length:
                return True
            
            for j in range(min(i + maxJump, length), i + minJump - 1, -1):
                if j in visited:
                    continue
                visited.add(j)
            #for j in range(i + minJump, min(i + maxJump, length) + 1):
                # print(j)
                if s[j] == '0':
                    if jump(j):
                        return True
            
            return False

        return jump(0)
            
        


        