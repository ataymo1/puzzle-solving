class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dp(index, cur):
            if index == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0

            return dp(index + 1, cur - nums[index]) + dp(index + 1, cur + nums[index])

        return dp(0, 0)