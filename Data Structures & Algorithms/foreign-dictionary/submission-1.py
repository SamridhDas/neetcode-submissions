class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj=defaultdict(list)
        indeg={c:0 for word in words for c in word}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        indeg[w2[j]]+=1
                    break
        q=deque()
        for c in indeg:
            if indeg[c]==0:
                q.append(c)
        res=[]
        while q:
            c=q.popleft()
            res.append(c)
            for nei in adj[c]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        if len(res) != len(indeg):
            return ""

        return "".join(res)
        



            