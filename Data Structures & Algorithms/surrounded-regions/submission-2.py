class Solution:
    def solve(self, board: List[List[str]]) -> None:

        res = set()

        def surrounded(row, col, visited, add):
            if row == 0 or col == 0 or row == len(board) - 1 or col == len(board[0]) - 1:
                return False
            visited.add((row, col))
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for n in neighbors:
                i, j = n
                if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == 'X':
                    continue
                if n in visited:
                    continue
                if not surrounded(i, j, visited, add):
                    return False
            add.add((row, col))
            return True

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == 'O':
                    add = set()
                    if surrounded(i, j, set(), add):
                        res |= add
        

        for row, col in res:
            board[row][col] = 'X'



