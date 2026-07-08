class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj=defaultdict(list)
        deg=[0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            deg[u]+=1
            deg[v]+=1
        q=deque()
        for i in range(n):
            if deg[i]==1:
                q.append(i)
        r=n
        while r>2:
            r=r-len(q)
            for i in range(len(q)):
                node=q.popleft()
                for nei in adj[node]:
                    deg[nei]-=1
                    if deg[nei]==1:
                        q.append(nei)
        return list(q)
    
