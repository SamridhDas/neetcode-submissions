class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        
        map={"2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"}
        def dfs(path,i):
            if i==len(digits):
                res.append("".join(path[:]))
                return 
            for c in (map[digits[i]]):
                path.append(c)
                dfs(path,i+1)
                path.pop()
        
        
        if digits:
            dfs([],0)
            return res
        else:
            return []
        



        

