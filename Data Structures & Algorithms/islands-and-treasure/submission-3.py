class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        INF = 2147483647
        rows=len(grid)
        cols=len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if(nr<0 or nr>=rows or nc<0 or nc>=cols or grid[nr][nc]!=INF):
                    continue
                grid[nr][nc]=1+grid[r][c]
                q.append((nr,nc))
        