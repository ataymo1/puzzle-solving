class Solution:
    def scoreOfString(self, s: str) -> int:

        prev = ord(s[0])
        total = 0

        for i in range(1, len(s)):
            total += abs(ord(s[i]) - prev)
            prev = ord(s[i])

        return total

        