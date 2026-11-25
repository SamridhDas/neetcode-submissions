class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        INF=2147483647
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    q.append((r,c))
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                new_r=r+dr
                new_c=c+dc
                if new_r<0 or new_r>=rows or new_c<0 or new_c>=cols or grid[new_r][new_c]!=INF:
                    continue
                grid[new_r][new_c]=1+grid[r][c]
                q.append((new_r,new_c))
        