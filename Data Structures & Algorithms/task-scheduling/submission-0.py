class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap=[ -num for num in  count.values()]
        heapq.heapify(maxheap)
        time=0
        q=deque()
        while maxheap or q:
            time+=1
            if maxheap:
                count=heapq.heappop(maxheap)+1
                if count:
                    q.append([count,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time
                

