class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[0]*(n+1)
        for i in range(1,n+1):
            arr[i]=arr[i-1]+1
        res=[]
        for num in arr:
            count=0
            while num:
                count+=num%2
                num=num//2
            res.append(count)
        return res
        
    