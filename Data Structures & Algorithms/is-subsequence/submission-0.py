class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif not t:
            return False

        letter_pointer = 0

        for l in t:
            if l == s[letter_pointer]:
                letter_pointer += 1
            if letter_pointer == len(s):
                return True
        
        return False
        