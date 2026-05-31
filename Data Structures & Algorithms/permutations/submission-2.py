class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms=[[]]

        for n in nums:
            new_perms=[]
            for p in perms:
                for i in range(len(p)+1):
                    perm_copy=p.copy()
                    perm_copy.insert(i,n)
                    new_perms.append(perm_copy)
            perms=new_perms
        
        return perms

                


        