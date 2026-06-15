class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i = 0
        length = len(t)
        for l in s:
            if t[i] == l:
                i += 1
            if i == length:
                return 0


        return length - i
        