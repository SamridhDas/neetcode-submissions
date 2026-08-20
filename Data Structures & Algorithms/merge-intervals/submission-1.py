class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        for s,f in intervals:
            if not res or s>res[-1][1]:
                res.append([s,f])
            else:
                res[-1][1]=max(res[-1][1],f)
        return res