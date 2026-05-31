class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        res=[]
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in seen:
                res.append(seen[complement])
                res.append(i)
                return res

            seen[nums[i]]=i
        




      
        