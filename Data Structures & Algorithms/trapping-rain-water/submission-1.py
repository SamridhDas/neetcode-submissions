class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        leftmax=height[l]
        rightmax=height[r]
        while l<r:
            if(leftmax<rightmax):
                curr=leftmax-height[l]
                if curr>0:
                    res+=curr
                l+=1
                leftmax=max(leftmax,height[l])
            else:
                curr=rightmax-height[r]
                if curr>0:
                    res+=curr
                r-=1
                rightmax=max(rightmax,height[r])
        return res
