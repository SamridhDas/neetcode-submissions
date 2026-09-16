class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        while l<r:
            capacity=(l+r)//2
            time=1
            total=0
            for i in range(len(weights)):
                if weights[i]+total>capacity:
                    time+=1
                    total=0
                total+=weights[i]
            if time>days:
                l=capacity+1
            else:
                res=min(capacity,res)
                r=capacity
        return res

            
                
                    
