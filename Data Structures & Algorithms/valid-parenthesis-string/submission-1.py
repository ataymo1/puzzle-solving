class Solution:
    def checkValidString(self, s: str) -> bool:

        cur = 0
        for l in s:
            if l == ')':
                if cur > 0 :
                    cur -= 1
                else:
                    return False
            else:
                cur += 1
        
        cur = 0
        for l in reversed(s):
            if l == '(':
                if cur > 0:
                    cur -= 1
                else:
                    return False
            else:
                cur += 1

        
        return True

        