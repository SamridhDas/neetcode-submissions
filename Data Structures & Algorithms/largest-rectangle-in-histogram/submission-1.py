class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,curr=stack.pop()
                area=curr*(i-index)
                res=max(area,res)
                start=index
            stack.append((start,h))
        for i,h in stack:
            res=max(res,h*(len(heights)-i))
        return res
        
