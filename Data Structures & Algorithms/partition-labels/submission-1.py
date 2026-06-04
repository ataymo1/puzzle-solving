from collections import OrderedDict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        letters = OrderedDict()

        for i, l in enumerate(s):
            if l in letters:
                letters[l][1] = i
            else:
                letters[l] = [i, i]

        # print(letters)
        start, end = -1, -1
        sol = []
        for new_start, new_end in letters.values():
            # print(f"{new_start} : {new_end}")
            if end == -1:
                start, end = new_start, new_end
                continue
            if start < new_start < end:
                end = max(end, new_end)
            else:
                sol.append(end - start + 1)
                start = new_start
                end = new_end
        
        sol.append(end - start + 1)
        return sol

            
        