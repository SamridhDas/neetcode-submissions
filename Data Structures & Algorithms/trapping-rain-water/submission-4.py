class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        leftmax=height[l]
        rightmax=height[r]
        res=0
        while (l<=r):
            if leftmax<rightmax:
                leftmax=max(leftmax,height[l])
                res+=leftmax-height[l]
                l+=1
            else:
                rightmax=max(rightmax,height[r])
                res+=rightmax-height[r]
                r-=1
        return res
