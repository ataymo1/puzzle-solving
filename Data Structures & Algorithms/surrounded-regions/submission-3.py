class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def mark(row, col):
            board[row][col] = 'T'
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            for n in neighbors:
                i, j = n
                if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and board[i][j] == 'O':
                   mark(i, j)
                
        for i in range(len(board)):
            if board[i][0] == 'O':
                mark(i, 0)

        for i in range(len(board)):
            if board[i][-1] == 'O':
                mark(i, len(board[0]) - 1)

        for j in range(len(board[0])):
            if board[0][j] == 'O':
                mark(0, j)

        for j in range(len(board[0])):
            if board[-1][j] == 'O':
                mark(len(board) - 1, j)


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                

        



