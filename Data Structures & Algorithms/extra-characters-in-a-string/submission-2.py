class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class Trie:
    def __init__(self,words):
        self.root=TrieNode()
        for w in words:
            curr=self.root
            for c in w:
                if c  not in curr.children:
                    curr.children[c]=TrieNode()
                curr=curr.children[c]
            curr.end=True
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dp={len(s):0}
        trie=Trie(dictionary).root

        def dfs(start):
            
            if start in dp:
                return dp[start]
            res=1+dfs(start+1)
            curr=trie
            for i in range(start,len(s)):
                if s[i] not in curr.children:
                    break
                curr=curr.children[s[i]]
                if curr.end:
                    res=min(res,dfs(i+1))
            dp[start]=res
            return res
        return dfs(0)