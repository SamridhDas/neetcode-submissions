class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(path,o,c):
            if o==c==n:
                res.append("".join(path))
                return
            if o<n:
                path.append('(')
                dfs(path,o+1,c)
                path.pop()
            if c<o:
                path.append(')')
                dfs(path,o,c+1)
                path.pop()
        dfs([],0,0)
        return res