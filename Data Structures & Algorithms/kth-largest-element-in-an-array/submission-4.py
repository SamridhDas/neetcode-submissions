class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap=[]
        heapq.heapify(maxheap)
        for num in nums:
            heapq.heappush(maxheap,-num)
        while k>0:
            res=heapq.heappop(maxheap)
            res*=-1
            k-=1
        return res
        

