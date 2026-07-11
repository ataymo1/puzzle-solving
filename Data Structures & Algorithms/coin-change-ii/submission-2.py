'''
base cases:
finished coin index, above amount, at amount

steps: take a coin, skip the coin

take a coin:
    amount - coin[i], index 

skip a coin:
    amount, index + 1

'''
from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # coin index x amount
        mem = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        coins.sort()
        # do first row

        for i in range(len(mem[0])):
            mem[0][i] = 1 if i % coins[0] == 0 else 0

        for i in range(len(mem)):
            mem[i][0] = 1

        for i in range(1, len(mem)):
            for j in range(1, len(mem[0])):
                skip = mem[i-1][j]
                take = 0
                if j - coins[i] >= 0:
                    take = mem[i][j - coins[i]]
                mem[i][j] = skip + take
                
        return mem[-1][-1]
            
    


        