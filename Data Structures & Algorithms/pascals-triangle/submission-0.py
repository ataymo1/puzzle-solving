class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        sol = [[1]]
        for i in range(1, numRows):
            row = [1]

            for j in range(1, len(sol[i-1])):
                row.append(sol[i-1][j] + sol[i-1][j-1])
            
            row.append(1)
            sol.append(row)

        return sol
        