class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1, min2 = 1e9, 1e9
        for price in prices:
            check = 1e9
            if price < min1:
                if min1 < min2:
                    min2 = min1
                min1 = price
            elif price < min2:
                min2 = price
        
        res = money - min1 - min2

        return res if res >= 0 else money





        