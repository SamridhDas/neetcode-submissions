class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        n=len(nums)/3
        res=[]
        for num in nums:
            count[num]=1+count.get(num,0)
            if  num not in res and count[num]>n:
                res.append(num)
        return res