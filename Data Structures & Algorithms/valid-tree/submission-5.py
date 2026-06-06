class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            if n == 1:
                return True
            else:
                return False
        children = {}
        maxVisited = 0
        for i in range(n):
            children[i] = set()

        # print(children)
        for one, two in edges:
            if one == two:
                return False
            children[one].add(two)
            children[two].add(one)

        def checkCycle(par, cur, visited, amountVisited):
            nonlocal maxVisited
            if cur in visited:
                return True
            visited.add(cur)
            for child in children[cur]:
                if child != par:
                    amountVisited += 1
                    if checkCycle(cur, child, visited, amountVisited):
                        return True
            maxVisited = max(maxVisited, amountVisited)
            return False

        for i in range(n):
            if checkCycle(i, i, set(), 1):
                return False
        if maxVisited != n:
            # print(f"{maxVisited}")
            return False

        return True

                    


        