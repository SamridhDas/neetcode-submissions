class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can(test):
            s=0
            curr=0
            for num in nums:
                curr+=num
                if curr>test:
                    s+=1
                    curr=num
            return s+1<=k

        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            m=(l+r)//2
            if can(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res