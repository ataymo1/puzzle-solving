class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        found = defaultdict(int)
        heap = []
        for num in nums:
            found[num] += 1
            heapq.heappush(heap, -num)
        
        while heap:
            num = -heapq.heappop(heap)
            if found[num] == 1:
                return num

        return -1            
        