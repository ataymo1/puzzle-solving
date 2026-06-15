class Solution:
    def scoreOfString(self, s: str) -> int:

        prev = ord(s[0])
        total = 0

        for i in range(1, len(s)):
            cur = ord(s[i])
            total += abs(cur - prev)
            prev = cur

        return total

        