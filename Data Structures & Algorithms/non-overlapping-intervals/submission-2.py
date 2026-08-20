class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x:x[1])
        count=0
        final=float("-inf")
        for s,f in intervals:
            if s>=final:
                final=f
                count+=1

        return len(intervals)-count
                
           