class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        foundOne, foundTwo, foundThree = False, False, False
        targetOne, targetTwo, targetThree = target
        
        for one, two, three in triplets:
            if one == targetOne and two <= targetTwo and three <= targetThree:
                foundOne = True
                if two == targetTwo:
                    foundTwo = True
                if three == targetThree:
                    foundThree = True
            if one <= targetOne and two == targetTwo and three <= targetThree:
                foundTwo = True
                if one == targetOne:
                    foundOne = True
                if three == targetThree:
                    foundThree = True
            if one <= targetOne and two <= targetTwo and three == targetThree:
                foundThree = True
                if one == targetOne:
                    foundOne = True
                if two == targetTwo:
                    foundTwo = True

            if foundOne and foundTwo and foundThree:
                return True
        
        return False
                

        