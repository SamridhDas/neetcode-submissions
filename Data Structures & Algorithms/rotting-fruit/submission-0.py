class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        dir=[[0,1],[0,-1],[1,0],[-1,0]]
        fresh=0
        time=0
        q=deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append([r,c])
                    
        
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                
                for dr,dc in dir:
                    if(r+dr>=rows or r+dr<0 or c+dc>=cols or c+dc<0 or grid[r+dr][c+dc]!=1):
                        continue
                    grid[r+dr][c+dc]=2
                    q.append([r+dr,c+dc])
                    fresh-=1
            time+=1
        if fresh==0:
            return time
        else:
            return -1


