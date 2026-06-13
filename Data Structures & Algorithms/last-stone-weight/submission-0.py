class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=stones
        for i in range(len(stones)):
            stones[i]*=-1
        heapq.heapify(stones)
        while len(maxheap)>1:
            a=-(heapq.heappop(stones))
            b=-(heapq.heappop(stones))
            if a!=b:
                heapq.heappush(maxheap,-abs(b-a))
        if not maxheap:
            return 0
        else:
            return -(maxheap[0])
        