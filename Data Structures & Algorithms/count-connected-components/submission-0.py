class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for i in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited=set()
        count=0
        def dfs(i):
            visited.add(i)
            for n in adj[i]:
                if n not in visited:
                    dfs(n)
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        return count 
        
        
        

           
