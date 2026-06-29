class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visit=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if  r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit or grid[r][c]=="0":
                return 
            visit.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    ans+=1
                    dfs(r,c)
        return ans


