class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(path,c,o):
            if len(path)==2*n:
                res.append("".join(path[:]))
                return
            if o<n:
                path.append("(")
                dfs(path,c,o+1)
                path.pop()
            if c<n and o>c:
                path.append(")")
                dfs(path,c+1,o)
                path.pop()
        dfs([],0,0)
        return res