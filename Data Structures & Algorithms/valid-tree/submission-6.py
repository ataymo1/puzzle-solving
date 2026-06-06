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

        # print(children)
        for one, two in edges:
            if one == two:
                return False
            children[one].add(two)
            children[two].add(one)

        def checkCycle(par, cur, visited, amountVisited):
            if cur in visited:
                return -1
            visited.add(cur)
            for child in children[cur]:
                if child != par:
                    # print(f"{par} : {child}")
                    amountVisited = checkCycle(cur, child, visited, amountVisited + 1)
                    if amountVisited == -1:
                        return -1
            return amountVisited

        visited = checkCycle(0, 0, set(), 1)
        
        if visited != n:
            # print(f" not full {visited}")
            return False

        return True

                    


        