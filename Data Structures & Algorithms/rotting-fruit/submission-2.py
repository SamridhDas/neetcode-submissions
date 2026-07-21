
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        rows=len(grid)
        cols=len(grid[0])
        q=deque()
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        time=0
        while fresh>0 and q:
            for i in range(len(q)):
                x,y=q.popleft()
                for dr,dc in directions:
                    nr=x+dr
                    nc=y+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            time+=1
        if fresh==0:
            return time
        else:
            return -1