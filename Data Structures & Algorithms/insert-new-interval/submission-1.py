class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res=[]
        for s,f in intervals:
            if not res or s>res[-1][1]:
                res.append([s,f])
            else:
                res[-1][1]=max(f,res[-1][1])
        return res