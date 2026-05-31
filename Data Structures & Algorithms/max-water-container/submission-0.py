class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_volm=0
        volm=0
        height=0
        while (l<r):
            height=min(heights[l],heights[r])
            volm=height*(r-l)
            if(max_volm<volm):
                max_volm=volm
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return max_volm