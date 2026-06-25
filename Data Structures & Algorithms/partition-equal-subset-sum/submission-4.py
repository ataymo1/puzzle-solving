class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        # array will be items x target

        mem = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(len(mem)):
            mem[i][0] = True

        for i in range(1, len(mem)):
            for j in range(1, len(mem[0])):

                # skip
                skip = mem[i-1][j]
                take = False
                if j - nums[i - 1] >= 0:
                    take = mem[i-1][j-nums[i-1]]

                mem[i][j] = take or skip
                

        return mem[-1][-1]
                



