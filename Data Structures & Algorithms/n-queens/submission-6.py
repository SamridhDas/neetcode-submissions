class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        posdia=set()
        negdia=set()
        res=[]
        board=[["."]*n for i in range(n)]

        def dfs(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
            for c in range(n):
                if c in cols or r+c in posdia or r-c in negdia:
                    continue
                board[r][c]="Q"
                cols.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                dfs(r+1)

                cols.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                board[r][c]="."
        dfs(0)
        return res
