from collections import deque
class MyStack:

    # def __init__(self):
        

    # def push(self, x: int) -> None:
        

    # def pop(self) -> int:
        

    # def top(self) -> int:
        

    # def empty(self) -> bool:
        

#class QueueStack:
    def __init__(self):
        self.a = deque()

    def push(self, x):
        n = len(self.a)
        self.a.append(x)
        for i in range(n):
            self.a.append(self.a.popleft())
 

    def pop(self):
        if len(self.a) > 0:
            k = self.a[0]
            self.a.popleft()
            return k 
        return None


    def top(self):
        if len(self.a) > 0:
            k = self.a[0]
            return k 
        return None

     

    def empty(self):
        return len(self.a) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()