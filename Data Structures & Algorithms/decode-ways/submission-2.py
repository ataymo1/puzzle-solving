from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dp(i):
            if i > len(s):
                return 0
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if s[i] == "1":
                return  dp(i + 1) + dp(i + 2)
            
            if s[i] == "2":

                if i == len(s) - 1:
                    return 1
                
                if int(s[i + 1]) <= 6:
                    return dp(i + 1) + dp(i + 2)
                

            return dp(i + 1)

        return dp(0)

        