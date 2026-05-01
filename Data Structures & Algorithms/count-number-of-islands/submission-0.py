class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island = 0
        visited = set()


        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            visited.add((start_r, start_c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and
                        nc in range(cols) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
        return island
            