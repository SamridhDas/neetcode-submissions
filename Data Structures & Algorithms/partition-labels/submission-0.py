class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex={}
        for i in range(len(s)):
            lastindex[s[i]]=i
        end=0
        start=0
        res=[]
        for  i in range(len(s)):
            end=max(end,lastindex[s[i]])
            if i==end:
                res.append(end-start+1)
                start=end+1
        return res