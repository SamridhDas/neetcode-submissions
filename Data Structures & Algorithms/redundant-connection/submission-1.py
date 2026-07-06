class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[None]*(len(edges)+1)
        size=[1]*(len(edges)+1)

        for i in range(len(parent)):
            parent[i]=i

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                return False
            if size[rootx]<size[rooty]:
                rootx,rooty=rooty,rootx
            parent[rooty]=rootx
            return True
        for u,v in edges:
            if not union(u,v):
                return [u,v]

    