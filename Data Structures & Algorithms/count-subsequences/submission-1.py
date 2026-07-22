class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        target_len = len(t)
        original_len = len(s)

        mem = [[0] * (original_len + 1) for _ in range(target_len + 1)]

        for i in range(original_len):
            mem[0][i] = 1

        for i in range(1, target_len + 1):
            for j in range(1, original_len + 1):
                mem[i][j] = mem[i][j-1]
                if t[i-1] == s[j-1]:
                    mem[i][j] += mem[i-1][j-1]
                
        return mem[-1][-1]


        