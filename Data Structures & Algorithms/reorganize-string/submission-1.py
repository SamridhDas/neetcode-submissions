class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        maxHeap=[]
        for char,c in count.items():
            maxHeap.append((-c,char))
        heapq.heapify(maxHeap)
        prev=None
        res=""
        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            c,char=heapq.heappop(maxHeap)
            res+=char
            c+=1

            if prev:
                heapq.heappush(maxHeap,prev)
                prev=None
            if c!=0:
                prev=(c,char)
        return res
