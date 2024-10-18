class Stack:
    # You can implement this class however you like
    def __init__(self) -> None:
        self.cap = 10000
        self.stack = [(None),(None)] * self.cap
        self.size = 0
    def pop(self)-> None:
        if self.size==0:
            raise Exception("Cannot pop from empty stack")
        else:
            self.stack[self.size-1] = -1
            self.size -=1
    def top(self):
        if self.size==0:
            raise Exception("Empty stack")
        else:
            return self.stack[self.size-1]
    def append(self,input):
        if self.size==self.cap:
            self.cap *= 2
            temp = self.stack[:]
            self.stack = [(None,None)]*self.cap
            for i in range(len(temp)):
                self.stack[i] = temp[i]
            temp = None
        self.size+=1
        self.stack[self.size-1]=input    
    def isEmpty(self):
        if self.size==0:
            return True
        return False
    def length(self):
        return self.size
    def show(self):
        return self.stack[:self.size]

    
    