class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        def backtrack(index,path):
            if len(nums)==index:
                x=0
                if path:
                    for num in path:
                        x^=num
                res.append(x)
                return
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()

            backtrack(index+1,path)
        backtrack(0,[])
        return sum(res)


