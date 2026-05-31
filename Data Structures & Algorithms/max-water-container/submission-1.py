class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l=0
        r=n-1
        res=0
        while l<r:
            height=min(heights[l],heights[r])
            width=(r-l)
            curr=height*width
            res=max(curr,res)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return res
