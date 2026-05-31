class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(",
        "}":"{","]":"["} #close:open
        stack=[]
        for b in s:
            if b in hashmap:
                if stack and stack[-1]==hashmap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if stack:
            return False
        else:
            return True