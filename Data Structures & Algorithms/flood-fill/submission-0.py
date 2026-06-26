class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        toChange = image[sr][sc]

        if color == toChange:
            return image

        queue = deque()
        queue.append([(sr, sc)])
        visited = set()

        while queue:
            cur_level = queue.popleft()
            next_level = []
            for row, col in cur_level:
                image[row][col] = color
                neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                visited.add((row, col))

                for n in neighbors:
                    n_row, n_col = n
                    if n in visited or n_row < 0 or n_row >= len(image) or n_col < 0 or n_col >= len(image[0]):
                        continue
                    if image[n_row][n_col] != toChange:
                        continue

                    next_level.append(n)
                if next_level:
                    queue.append(next_level)
        
        return image
                    



        