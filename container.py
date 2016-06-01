class Stack(object):
    def __init__(self):
        self.list = []
        self.size = 0
    def push(self, val):
        self.size += 1
        self.list.append(val)
    def pop(self):
        if self.size > 0:
            self.size -= 1
            top = self.list[-1]
            self.list = self.list[:-1]
            return top
    def top(self):
        return self.list[-1]

class Queue(object):
    def __init__(self):
        self.list = []
        self.size = 0
    def enq(self, val):
        self.size += 1
        self.list.append(val)
    def deq(self):
        if self.size > 0:
            self.size -= 1
            k = self.list[0]
            self.list = self.list[1:]
            return k
    def front(self):
        return self.list[0]


stk = Stack()
stk.push(5)
stk.push(3)
stk.push(7)

for x in range(stk.size):
    print stk.pop()

que = Queue()
que.enq(2)
que.enq(4)
que.enq(7)

for x in range(que.size):
    print que.deq()





