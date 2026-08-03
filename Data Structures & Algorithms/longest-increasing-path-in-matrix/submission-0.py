class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        dp={}
        directions=[(0,1),(-1,0),(1,0),(0,-1)]
        def dfs(r,c,prev):
            if r<0 or r>=rows or c<0 or c>=cols or matrix[r][c]<=prev:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res=1
            for dr,dc in directions:
                
                res=max(res,1+dfs(r+dr,c+dc,matrix[r][c]))
            dp[(r,c)]=res
            return dp[(r,c)]
        ans=1
        for r in range(rows):
            for c in range(cols):
                ans=max(ans,dfs(r,c,float('-inf')))
        return ans


                
            