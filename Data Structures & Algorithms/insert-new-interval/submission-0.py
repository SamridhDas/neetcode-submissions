class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    
        def merge(intervals):
            res=[]
            for s,f in intervals:
                if not res or s>res[-1][1]:
                    res.append([s,f])
                else:
                    res[-1][1]=max(res[-1][1],f)
            return res
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        return merge(intervals)
