class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        visit=set()
        for a,b in prerequisites:
            graph[a].append(b)
        def dfs(u):
            if u in visit:
                return False
            if graph[u]==[]:
                return True
            visit.add(u)
            for v in graph[u]:
                if not dfs(v):
                    return False
            visit.remove(u)
            graph[u]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
