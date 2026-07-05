class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        s_ = set(nums)

        return len(s_) != len(nums)
        