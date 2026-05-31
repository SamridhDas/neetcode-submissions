class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        res=[]
        
        
        while(r<len(nums)):
            max_num=None
            
            for left in range(l,r+1):
                if max_num==None:
                    max_num=nums[left]
                else:
                    max_num=max(max_num,nums[left])
            l+=1
            r+=1
            res.append(max_num)

           
        return res
