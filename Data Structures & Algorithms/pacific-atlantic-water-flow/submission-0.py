
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(starts):

            visited = set(starts)
            stack = starts[:]

            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (0 <= nr < rows and
                        0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]):

                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return visited

        pacific_starts = []
        atlantic_starts = []

        for c in range(cols):
            pacific_starts.append((0, c))
            atlantic_starts.append((rows - 1, c))

        for r in range(rows):
            pacific_starts.append((r, 0))
            atlantic_starts.append((r, cols - 1))

        pacific = dfs(pacific_starts)
        atlantic = dfs(atlantic_starts)

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
