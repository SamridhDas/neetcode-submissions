class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows=len(heights)
        cols=len(heights[0])
        pac=set()
        atl=set()
        def dfs(r,c,ocean,prev):
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            if r<0 or r>=rows or c<0 or c>=cols or heights[r][c]<prev or (r,c)in ocean:
                return
            ocean.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc,ocean,heights[r][c])
            
        for r in range(rows):
            dfs(r,0,pac,-1)
            dfs(r,cols-1,atl,-1)
        for c in range(cols):
            dfs(0,c,pac,-1)
            dfs(rows-1,c,atl,-1)
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in atl and (r,c) in pac:
                    res.append((r,c))
        return res

                
