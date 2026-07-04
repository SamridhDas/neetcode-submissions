class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        dist=[[float('infinity')]* cols for i in range(rows)]
        minheap=[]
        heapq.heapify(minheap)
        heapq.heappush(minheap,(0,0,0))
        
        while minheap:
            effort,r,c=heapq.heappop(minheap)
            if r==rows-1 and c==cols-1:
                return effort
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if nr<0 or nr>=rows or nc<0 or nc>=cols:
                    continue
                new_effort=max(effort,abs(heights[r][c]-heights[nr][nc]))
                if dist[nr][nc]>new_effort:
                    dist[nr][nc]=new_effort
                    heapq.heappush(minheap,(new_effort,nr,nc))
        
            

    
        