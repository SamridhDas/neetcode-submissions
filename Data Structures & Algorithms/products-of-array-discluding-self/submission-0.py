class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            multiple=1
            for j in range (len(nums)):
                if(j==i):
                    continue
                else:
                    multiple*=nums[j]
            res.append(multiple)
        return res
                
        
        


        