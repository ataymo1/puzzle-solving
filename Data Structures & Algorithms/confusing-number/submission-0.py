class Solution:
    def confusingNumber(self, n: int) -> bool:

        pair = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        n = str(n)
        confusing = False
        for i in range(len(n)):
            if n[i] not in pair:
                return False

            if n[i] != pair[n[-i - 1]]:
                confusing = True

        return confusing
