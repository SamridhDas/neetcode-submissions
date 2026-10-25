class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area=0
        rows=len(grid)
        cols=len(grid[0])
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        
        


        def dfs(r,c):
            
            ans=1
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0):
                return 0
            
            grid[r][c]=0
            
            for dr,dc in dir:
                ans+=dfs(r+dr,c+dc)
            
            return ans 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    
                    area=max(area,dfs(r,c))
        return area
