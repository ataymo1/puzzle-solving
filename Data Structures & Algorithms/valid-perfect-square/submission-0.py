class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            check = mid**2
            # print(r)
            # print(l)
            # print(mid)

            if check == num:
                return True
            
            if check > num:
                r = mid - 1
            elif check < num:
                l = mid + 1
        return False

        