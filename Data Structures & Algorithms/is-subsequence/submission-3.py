class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        length = len(s)

        letter_pointer = 0

        for l in t:
            if l == s[letter_pointer]:
                letter_pointer += 1
            if letter_pointer == length:
                return True
        
        return False
        