class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=0
        while l<=r:
            m=(l+r)//2
            total=0
            time=1
            for w in weights:
                
                if total+w>m:
                    time+=1
                    total=0
                total+=w
            if time<=days:
                res=m
                r=m-1
            else:
                l=m+1
        return res

            