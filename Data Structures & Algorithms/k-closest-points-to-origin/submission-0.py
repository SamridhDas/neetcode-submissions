class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        minheap=[]
        for x,y in points:
            dist=(x**2+y**2)**0.5
            minheap.append((dist,x,y))
        heapq.heapify(minheap)
        i=0
        if len(minheap)<k:
            while len(minheap):
                a,b,c=heapq.heappop(minheap)
                res.append((b,c))
        else:
            while i<k:
                a,b,c=heapq.heappop(minheap)
                res.append((b,c))
                i+=1
        return res