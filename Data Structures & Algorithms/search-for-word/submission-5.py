class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        path=set()
        rows,cols=len(board),len(board[0])
        def dfs(i,r,c):
            if i==len(word):
                return True
            if r<0 or c<0 or c>=cols or r>=rows or board[r][c]!=word[i] or (r,c) in path:
                return False
            path.add((r,c))
            for dr,dc in directions:
                if dfs(i+1,r+dr,c+dc):
                    return True
            path.remove((r,c))
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(0,r,c):
                    return True
        return False

