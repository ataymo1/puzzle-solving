class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        numbers = set(arr)
        total = 0
        for n in arr:
            if n + 1 in numbers:
                total += 1
        
        return total