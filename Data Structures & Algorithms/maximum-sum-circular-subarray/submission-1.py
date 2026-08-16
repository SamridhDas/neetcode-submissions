class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max=0
        curr_min=0
        mini=float("inf")
        maxy=float("-inf")
        total=sum(nums)
        for num in nums:
            curr_max=max(curr_max+num,num)
            curr_min=min(curr_min+num,num)
            mini=min(mini,curr_min)
            maxy=max(maxy,curr_max)
        if maxy<0:
            return maxy
        return max(maxy,total-mini)
            