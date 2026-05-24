class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        neighbors = {}
        heap = []
        visited = [0] * n

        for i in range(n):
            neighbors[i] = set()

        for start, end, cost in flights:
            neighbors[start].add((cost, end))

        visited[src] = 1
        for cost, end in neighbors[src]:
            heapq.heappush(heap, (cost, 0, end))
        
        if not heap:
            return -1

        while heap:
            spent, steps, cur = heapq.heappop(heap)
            if steps > k:
                continue
            if cur == dst:
                return spent
            visited[cur] = spent
            for price, neighbor in neighbors[cur]:
                if visited[neighbor] > 0:
                    continue
                heapq.heappush(heap, (spent + price, steps + 1, neighbor))
        
        return -1


        

        