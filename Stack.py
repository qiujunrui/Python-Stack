class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def is_empty(self):
        if self.items==[]:
            return True
        else:
            return False
    def pop(self):
        if self.items==[]:
            return False
        else:
            n=self.items[-1]
            del self.items[-1]
            return n
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
