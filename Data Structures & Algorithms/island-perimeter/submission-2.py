class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visit=set()
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))

            peri=0
            for dr,dc in directions:
                peri+=dfs(r+dr,c+dc)
            return peri
        res=0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]==1:
                    res+=dfs(r,c)
        return res

