class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        
        res = 1
        if n > 0:
            for i in range(n):
                res *= x
                print(res)
        else:
            for i in range(abs(n)):
                res /= x
        
        return res
        