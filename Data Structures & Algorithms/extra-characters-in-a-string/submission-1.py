class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words=set(dictionary)
        dp={len(s):0}

        def dfs(start):
            
            if start in dp:
                return dp[start]
            res=1+dfs(start+1)
            for i in range(start,len(s)):
                if s[start:i+1] in words:
                    res=min(res,dfs(i+1))
            dp[start]=res
            return res
        return dfs(0)