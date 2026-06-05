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
        for i in range(len(s)-1, -1, -1):
            l = s[i]
            if l == '(':
                if cur > 0:
                    cur -= 1
                else:
                    return False
            else:
                cur += 1

        
        return True

        