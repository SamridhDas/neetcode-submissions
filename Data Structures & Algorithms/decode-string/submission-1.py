class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c==']':
                k=""
                while  stack[-1]!="[":
                    k=stack.pop()+k
                stack.pop()
                x=""
                while stack and stack[-1].isdigit():
                    x=stack.pop()+x
                stack.append(int(x)*k)
            else:
                stack.append(c)
        return "".join(stack)
