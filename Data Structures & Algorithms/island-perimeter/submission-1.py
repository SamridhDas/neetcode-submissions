class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
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
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    ans+=dfs(r,c)
        return ans

                


