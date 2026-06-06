class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            else:
                return False
        children = {}
        for i in range(n):
            children[i] = set()

        for one, two in edges:
            if one == two:
                return False
            children[one].add(two)
            children[two].add(one)

        def checkCycle(prev_node, cur_node, visited, amountVisited):
            if cur_node in visited:
                return -1
            visited.add(cur_node)
            for next_node in children[cur_node]:
                if next_node != prev_node:
                    amountVisited = checkCycle(cur_node, next_node, visited, amountVisited + 1)
                    if amountVisited == -1:
                        return -1
            return amountVisited

        visited = checkCycle(0, 0, set(), 1)
        
        if visited != n:
            return False

        return True

                    


        