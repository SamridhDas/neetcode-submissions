class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols=len(grid),len(grid[0])
        islands=0
        visit=set()

        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                r,c=q.popleft()
                for dr,dc in dir:
                    if((r+dr) in range(rows) and (c+dc) in range (cols) and grid[r+dr][c+dc]=="1" and (r+dr,c+dc) not in visit):
                        q.append((r+dr,c+dc))
                        visit.add((r+dr,c+dc))


        



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1
        return islands

        


