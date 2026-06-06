from functools import cache
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        visited = {}
        if s[-1] != '0':
            return False

        length = len(s) - 1
        
        def jump(i):
            if i in visited:
                return visited[i]
            if i == length:
                return True
            
            for j in range(min(i + maxJump, length), i + minJump - 1, -1):
                
                if s[j] == '0':
                    if jump(j):
                        visited[i] = True
                        return True
            visited[i] = False
            return False

        return jump(0)
            
        


        