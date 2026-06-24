class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dp(index, cur):
            if (index, cur) in cache:
                return cache[(index, cur)]
            if index == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0

            cache[(index, cur)] = dp(index + 1, cur - nums[index]) + dp(index + 1, cur + nums[index])
            return cache[(index, cur)]

        return dp(0, 0)