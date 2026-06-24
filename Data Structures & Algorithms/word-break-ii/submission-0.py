class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        def dfs(start,path):
            if start==len(s):
                res.append(" ".join(path[:]))
                return 
            for i in range(start,len(s)):
                if s[start:i+1] in wordDict:
                    path.append(s[start:i+1])
                    dfs(i+1,path)
                    path.pop()
        dfs(0,[])
        return res
                
