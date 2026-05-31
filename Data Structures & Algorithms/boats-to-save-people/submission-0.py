class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        people.sort()
        l=0
        r=len(people)-1
        while(l<=r):
            remain=limit-people[r]
            res+=1
            if l<r and remain>=people[l]:
                l+=1
            r-=1
        return res
