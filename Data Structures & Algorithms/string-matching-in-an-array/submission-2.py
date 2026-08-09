class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=set()
        words.sort(key=lambda x:len(x))
        for i in range(len(words)):
            word1=words[i]
            for j in range(i+1,len(words)):
                word2=words[j]
                if word1 in word2:
                    res.add(word1)
        return list(res)