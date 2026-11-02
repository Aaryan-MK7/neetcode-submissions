
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        islands = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":

                    islands += 1

                    stack = [(r, c)]
                    grid[r][c] = "0"

                    while stack:
                        row, col = stack.pop()

                        directions = [
                            (1, 0),
                            (-1, 0),
                            (0, 1),
                            (0, -1)
                        ]

                        for dr, dc in directions:
                            nr = row + dr
                            nc = col + dc

                            if (0 <= nr < rows and
                                0 <= nc < cols and
                                grid[nr][nc] == "1"):

                                grid[nr][nc] = "0"
                                stack.append((nr, nc))

        return islands
