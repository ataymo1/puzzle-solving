class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = len(coins)
        if amount == 0:
            return 0

        # will either take the coin or leave it

        cache = {}

        def dp(index, cur_amount):
            if (index, cur_amount) in cache:
                return cache[(index, cur_amount)]
            
            if cur_amount == amount:
                return 0
            elif cur_amount > amount:
                return 1e9
            
            if index >= length:
                return 1e9

            cache[(index, cur_amount)] = min(1 + dp(index, cur_amount + coins[index]), dp(index + 1, cur_amount))

            return cache[(index, cur_amount)]

        res = dp(0, 0)

        if res == 1e9:
            return -1
        return res
            



