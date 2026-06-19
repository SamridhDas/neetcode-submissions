class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        minHeap=[]
        seats=0
        for ppl,start,end in trips:
            while minHeap and minHeap[0][0]<=start:
                seats-=heapq.heappop(minHeap)[1]
            seats+=ppl
            if seats>capacity:
                return False
            heapq.heappush(minHeap,[end,ppl])
        return True



