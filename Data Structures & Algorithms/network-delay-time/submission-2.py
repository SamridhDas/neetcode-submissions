class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance=[float('infinity')]*(n+1)
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        distance[k]=0
        minheap=[]
        heapq.heapify(minheap)
        heapq.heappush(minheap,(0,k))
        while minheap:
            time,node=heapq.heappop(minheap)
            for v,w in adj[node]:
                if distance[v]>distance[node]+w:
                    distance[v]=distance[node]+w
                    heapq.heappush(minheap,(distance[v],v))
        res=-1
        for i in range(1,n+1):
            res=max(distance[i],res)
        if res==float('infinity'):
            return -1
        else:
            return res
