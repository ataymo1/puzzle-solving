class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        foundOne, foundTwo, foundThree = False, False, False
        targetOne, targetTwo, targetThree = target
        
        for one, two, three in triplets:
            if one > targetOne or two > targetTwo or three > targetThree:
                continue
            if one == targetOne:
                foundOne = True
            if two == targetTwo:
                foundTwo = True
            if three == targetThree:
                foundThree = True

            if foundOne and foundTwo and foundThree:
                return True
        
        return False
                

        