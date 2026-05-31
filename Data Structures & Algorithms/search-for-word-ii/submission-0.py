class Trie:
    def __init__(self):
        self.children={}
        self.word=False



    def addword(self,word):
        curr=self
        for c in word:
            if c not in curr.children:
                curr.children[c]=Trie()
            curr=curr.children[c]
        curr.word=True
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Trie()

        for w in words:
            root.addword(w)
        rows=len(board)
        cols=len(board[0])
        res=set()
        visit=set()
        def dfs(r,c,node,word):
            if r<0 or c<0 or r==rows or c==cols or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.word:
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

