class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        cur = nums[0]
        sol = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                cur += nums[i]
            else:
                cur = nums[i]
            sol = max(sol, cur)

        return sol
            

        