class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = 0

        for log in logs:
            if log == "../":
                stack = max(0, stack - 1)
            elif log == "./":
                continue
            else:
                stack += 1
        
        return stack


        