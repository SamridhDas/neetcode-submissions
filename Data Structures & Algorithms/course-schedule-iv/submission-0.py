class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for pre,crs in prerequisites:
            adj[crs].append(pre)
        def dfs(crs):
            if crs in premap:
                return premap[crs]
            premap[crs]=set()
            for prereq in adj[crs]:
                premap[crs]|=dfs(prereq)
            premap[crs].add(crs)
            return premap[crs]




        



        premap={}
        for crs in range(numCourses):
            dfs(crs)
        res=[]
        for u,v in queries:
            if u in  premap[v]:
                res.append(True)
            else:
                res.append(False)
        return res
        

        