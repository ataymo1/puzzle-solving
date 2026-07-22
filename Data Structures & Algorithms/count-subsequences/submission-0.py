from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        target_len = len(t)
        original_len = len(s)

        @cache
        def dp(original_index, target_index):
            if target_index == target_len:
                return 1
            
            if original_index == original_len:
                return 0

            if s[original_index] == t[target_index]:
                return dp(original_index + 1, target_index + 1) + dp(original_index + 1, target_index)
            
            return dp(original_index + 1, target_index)
        
        return dp(0, 0)
        