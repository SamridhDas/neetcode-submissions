class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=sum(weights)
        
        while l<=r:
            m=(l+r)//2
            time=1
            total=0
            for w in weights:
                if w+total>m:
                    time+=1
                    total=0
                total+=w
            if time<=days:
                res=m
                r=m-1
            else:
                l=m+1
        return res
            
            
