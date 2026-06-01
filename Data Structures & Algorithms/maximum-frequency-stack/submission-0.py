class FreqStack:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        self.hash={}
        

    def push(self, val: int) -> None:
        self.hash[val]=1+self.hash.get(val,0)
        self.stack1.append(val)

        

    def pop(self) -> int:
        max_freq=max(self.hash.values())
        while self.stack1:
            x=self.stack1.pop()
            if self.hash[x]!=max_freq:
                self.stack2.append(x)
            else:
                self.hash[x]-=1
                
                y=x
                break
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return y
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()