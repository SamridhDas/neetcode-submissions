class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        i=0
        n=len(path)
        while (i<n):
            if path[i]=='/':
                i+=1
                continue
            j=i
            while j<n and path[j]!='/':
                j+=1
            piece=path[i:j]
            if piece=='..' and stack:
                stack.pop()
            elif piece!='.' and piece!='..':
                stack.append(piece)
            i=j
        return '/'+'/'.join(stack)
        
            
