class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        mem = {}
        
        def backtrack(index, sides):
            hashable = tuple(sides)
            if hashable in mem:
                return mem[hashable]
            if index == len(matchsticks):
                square_length = sides[0]
                for i in range(1, len(sides)):
                    if square_length != sides[i]:
                        return False
                return True
            length = matchsticks[index]
            found = set()

            for i in range(len(sides)):
                if sides[i] in found:
                    continue
                found.add(sides[i])
                sides[i] = sides[i] + length
                if backtrack(index + 1, sides):
                    mem[hashable] = True
                    return True
                sides[i] -= length
            
            mem[hashable] = False
            return False
        
        return backtrack(0, [0, 0, 0, 0])

        