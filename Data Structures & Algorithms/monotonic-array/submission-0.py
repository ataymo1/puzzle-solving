class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        increasing = False
        decreasing = False

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if decreasing:
                    return False
                elif not increasing:
                    increasing = True
            elif nums[i] < nums[i-1]:
                if increasing:
                    return False
                elif not decreasing:
                    decreasing = True
        
        return True
        
        

        