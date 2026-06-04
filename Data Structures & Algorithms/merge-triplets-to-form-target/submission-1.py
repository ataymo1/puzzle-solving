class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        used = set()

        res = [0, 0, 0]
        targetOne, targetTwo, targetThree = target
        
        for one, two, three in triplets:
            if one == targetOne and two <= targetTwo and three <= targetThree:
                res[0] = targetOne
                if two == targetTwo:
                    res[1] = targetTwo
                if three == targetThree:
                    res[2] == targetThree
            if one <= targetOne and two == targetTwo and three <= targetThree:
                res[1] = targetTwo
                if one == targetOne:
                    res[1] = targetTwo
                if three == targetThree:
                    res[2] == targetThree
            if one <= targetOne and two <= targetTwo and three == targetThree:
                res[2] = targetThree
                if one == targetOne:
                    res[0] = targetOne
                if two == targetTwo:
                    res[1] == targetTwo
        
        if res[0] == 0 or res[1] == 0 or res[2] == 0:
            return False
        return True
                

        