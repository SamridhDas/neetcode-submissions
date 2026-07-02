class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        count={}
        freq=[[] for i in range(n+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for num in count:
            freq[count[num]].append(num)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            nums=freq[i]
            for num in nums:
                res.append(num)
                if len(res)==k:
                    return res
        return res

        