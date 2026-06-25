class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        count = [(0, 0)] * length
        for i, s in enumerate(strs):
            M, N = 0, 0
            for c in s:
                if c == '0':
                    M += 1
                else:
                    N += 1
            count[i] = (M, N)

        # Index x size m x size n

        mem = [[[0 for k in range(n + 1)] for j in range(m + 1)] for i in range(len(strs) + 1)]

        for i in range(1, len(mem)):
            for j in range(m + 1):
                for k in range(n + 1):
                    M, N = count[i - 1]
                    skip = mem[i - 1][j][k]
                    take = 0
                    if j >= M and k >= N:
                        take = mem[i - 1][j - M][k - N] + 1
                    mem[i][j][k] = max(skip, take)

        return mem[-1][-1][-1]
            
            
            

            
            




            
        