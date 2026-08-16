class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q=deque([0])
        visit=set()
        while q:
            index=q.popleft()
            if index==len(s)-1:
                return True
            for i in range(index+minJump,min(index+maxJump,len(s)-1)+1):
                if s[i]=="0":
                    if i in visit:
                        continue
                    else:
                        q.append(i)
                        visit.add(i)
        return False
