class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        if x==0:
            return 0
        l,r=1,x//2
        while l<=r:
            m=(l+r)//2
            pro=m*m
            if pro==x:
                return m
            elif pro<x:
                l=m+1
            else:
                r=m-1
        return l-1

