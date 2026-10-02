class Solution:
    def isPalindrome(self, x: int) -> bool:

        
        # go through the array
        # goal is going to be reconstructing the array
        if x < 0:
            return False
        num = 0
        x_copy = x

        while x > 0:
            num *= 10
            digit = x % 10
            num += digit
            x //= 10
        
        return True if x_copy == num else False



                
        