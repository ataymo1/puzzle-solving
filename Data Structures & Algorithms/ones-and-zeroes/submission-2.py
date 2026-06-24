from functools import cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [(0, 0)] * len(strs)
        for i, s in enumerate(strs):
            M, N = 0, 0
            for c in s:
                if c == '0':
                    M += 1
                else:
                    N += 1
            count[i] = (M, N)

        @cache
        def dp(index, cur_m, cur_n, size):

            if index == len(strs):
                return size

            r_m, r_n = count[index]
            
            keep = 0
            skip = dp(index + 1, cur_m, cur_n, size)
            if cur_m + r_m <= m and cur_n + r_n <= n:
                keep = dp(index + 1, cur_m + r_m, cur_n + r_n, size + 1)
            return max(keep, skip)

        return dp(0, 0, 0, 0)
            
            
            

            
            




            
        