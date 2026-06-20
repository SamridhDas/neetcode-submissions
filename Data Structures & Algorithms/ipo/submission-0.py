class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        q=deque()
        for i in range(len(profits)):
            q.append((capital[i],profits[i]))
        temp=list(q)
        temp.sort(key=lambda t:t[0])
        q=deque(temp)
        maxheap=[]
        while k>0:
            while q and  q[0][0]<=w:
                capital,profit=q.popleft()
                heapq.heappush(maxheap,-profit)
            if not maxheap:
                break
            
            p=-1*heapq.heappop(maxheap)
            w+=p
            k-=1
        return w