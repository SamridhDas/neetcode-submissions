class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        rows=len(grid)
        cols=len(grid[0])
        elevation=[[float('infinity')]*cols for i in range(rows)]
        elevation[0][0]=grid[0][0]
        minheap=[]
        heapq.heapify(minheap)
        heapq.heappush(minheap,(elevation[0][0],0,0))
        while minheap:
            time,r,c=heapq.heappop(minheap)
            if r==rows-1 and c==cols-1:
                return time
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                new_time=max(time,grid[nr][nc])
                if elevation[nr][nc]>new_time:
                    elevation[nr][nc]=time
                    heapq.heappush(minheap,(new_time,nr,nc))
        