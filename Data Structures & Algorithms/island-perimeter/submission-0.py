class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        self.perm=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]==0:
                return 1
            if (r,c) in visit:
                return 0
            visit.add((r,c))
            perm=0
            for dr,dc in directions:
                perm+=dfs(r+dr,c+dc)
            return perm
        peri=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                     peri+=dfs(r,c)
        return peri
            