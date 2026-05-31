class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        p=0
        
        for num in nums:
            count[num]=1+count.get(num,0)
        for i,c in count.items():
            if c>p:
                res=i
                p=c
        return res


