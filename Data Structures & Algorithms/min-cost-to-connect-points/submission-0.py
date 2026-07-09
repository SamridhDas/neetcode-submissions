class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res=0
        minheap=[]
        heapq.heapify(minheap)
        heapq.heappush(minheap,(0,0))
        visit=set()
        

        while minheap:
            cost,u=heapq.heappop(minheap)
            
            if u in visit:
                continue
            res+=cost
            visit.add(u)
            for i in range(0,len(points)):
                if i not in visit:
                    distance=abs(points[i][0]-points[u][0])+abs(points[i][1]-points[u][1])
                    heapq.heappush(minheap,(distance,i))
        return res
