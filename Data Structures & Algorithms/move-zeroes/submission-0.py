class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = 0
        total = 0

        for n in nums:
            if n == 0:
                total += 1
            else:
                nums[p] = n
                p += 1
        
        for i in range(len(nums) - total, len(nums)):
            nums[i] = 0

        