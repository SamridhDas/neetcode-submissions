class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while(l<=r):
            mid=nums[(l+r)//2]
            if mid==target:
                return (l+r)//2
            elif target>mid:
                l+=1
            else:
                r-=1

        return -1
