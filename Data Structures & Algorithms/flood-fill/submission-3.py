class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        toChange = image[sr][sc]

        if color == toChange:
            return image

        queue = deque()
        queue.append((sr, sc))

        while queue:
            row, col = queue.pop()
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            image[row][col] = color
            for n in neighbors:
                n_row, n_col = n
                if n_row < 0 or n_row >= len(image) or n_col < 0 or n_col >= len(image[0]):
                    continue
                if image[n_row][n_col] != toChange:
                    continue
                queue.append((n_row, n_col))
        
        return image
                    



        