from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        INF = 2147483647
        
        # 1. Find all treasures (0) and add them to our BFS starting queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c)) # Queue stores coordinates
        
        # 2. Radiate outwards from all treasures simultaneously
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # If the neighboring cell is in bounds and is an empty room (INF)
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                    # The shortest distance to this room is the current room's distance + 1
                    grid[nr][nc] = grid[r][c] + 1
                    # Append the neighbor so it can propagate to its own neighbors
                    q.append((nr, nc))
