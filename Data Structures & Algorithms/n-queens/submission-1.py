class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols=set()
        pos=set()
        neg=set()

        res=[]
        board=[["."]*n for i in range (n)]

        def queens(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 

            for c in range(n):
                if c in cols or (r+c) in pos or (r-c) in neg:
                    continue
                
                cols.add(c)
                pos.add(r+c)
                neg.add(r-c)
                board[r][c]="Q"


                queens(r+1)
                cols.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
                board[r][c]="."


        queens(0)
        return res

            