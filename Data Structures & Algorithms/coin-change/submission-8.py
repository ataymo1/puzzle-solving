from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # row is coin index
        # col is amount

        mem = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

        # set up first row

        for col in range(len(mem[0])):
            if col % coins[0] == 0:
                mem[0][col] = col // coins[0]
            else:
                mem[0][col] = 1e9

        for row in range(1, len(mem)):
            for col in range(1, len(mem[0])):
                skip = mem[row-1][col]
                take = 1e9
                if col - coins[row] >= 0:
                    take = 1 + mem[row][col - coins[row]]
                mem[row][col] = min(skip, take)
        

        return -1 if mem[-1][-1] == 1e9 else mem[-1][-1]
