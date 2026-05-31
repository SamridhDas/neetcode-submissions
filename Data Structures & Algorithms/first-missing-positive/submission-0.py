class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            freq[num]=1+freq.get(num,0)
        i=1
        while True:
            if i not in freq:
                return i
            i+=1