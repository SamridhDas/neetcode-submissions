class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF=float('infinity')
        dist=[INF]*(n+1)
        dist[k]=0
        adj=[[] for i in range(n+1)]
        for u,v,w in times:
            adj[u].append((v,w))
        minheap=[]
        heapq.heapify(minheap)
        heapq.heappush(minheap,(0,k))
        visit=set()
        while minheap:
            d,u=heapq.heappop(minheap)
            if u in visit:
                continue
            visit.add(u)
            for v,w in adj[u]:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
                    heapq.heappush(minheap,(dist[v],v))
        ans=-1
        for i in range(1,n+1):
            if dist[i]==INF:
                return -1

            if dist[i]>ans:
                ans=dist[i]
        return ans
