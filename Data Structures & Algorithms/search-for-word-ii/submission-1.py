class TrieNode():
    def __init__(self):
        self.children={}
        self.end=False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=TrieNode()
        for w in words:
            curr=root
            for c in w:
                if c not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.end=True
        rows=len(board)
        cols=len(board[0])
        res=set()
        visit=set()
        def dfs(r,c,node,word):
            if(r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or board[r][c] not in node.children):
                return
            visit.add((r,c))
            word+=board[r][c]
            node=node.children[board[r][c]]
            if node.end:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")
        return list(res)
