class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        res=0
        count=1
        for num in nums:
            if num-1 not in seen:
                temp=num
                while(temp+1) in seen:
                    temp+=1
                    count+=1
                res=max(res,count)
                count=1
        return res


