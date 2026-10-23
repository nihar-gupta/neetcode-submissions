class MyQueue:

    # def __init__(self):
        

    # def push(self, x: int) -> None:
        

    # def pop(self) -> int:
        

    # def peek(self) -> int:
        

    # def empty(self) -> bool:
        

#class StackQueue:
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)
        n = len(self.a)
        i = n-1
        while i>0:
            self.a[i], self.a[i-1] = self.a[i-1], self.a[i]
            i-=1


    def pop(self):
        if len(self.a) >0:
            k = self.a[-1]
            self.a.pop()
            return k
        return None


    def peek(self):
        if len(self.a) >0:
            k = self.a[-1]
            return k
        return None
        
     

    def empty(self):
        return len(self.a) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()