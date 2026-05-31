class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.minstack[-1]>=val:
            self.minstack.append(val)
        

    def pop(self) -> None:
       if self.stack[-1]==self.minstack[-1]:
            self.minstack.pop()

       return  self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        
