class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        half = total // 2

        def dp(index, sum1, sum2):
            if sum1 > half or sum2 > half:
                return False
            elif sum1 == half and sum2 == half:
                return True

            if index == len(nums):
                return False

            return dp(index + 1, sum1 + nums[index], sum2) or dp(index + 1, sum1, sum2 + nums[index])

        return dp(0, 0, 0)

                



