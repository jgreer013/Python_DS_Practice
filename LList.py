class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LList(object):
    def __init__(self, head=None, tail=None):
        self.size = 0
        self.head = head
        self.tail = tail

    def insert(self, node, loc=-1):
        if loc > self.size:
            raise ValueError("Index beyond Linked List bounds.")
        else:
            self.size += 1
            if self.head == None:
                self.head = node
            if self.tail == None:
                self.tail = node
            else:
                if loc == -1:
                    self.tail.next = node
                    self.tail = node
                else:
                    curr_node = self.head
                    prev_node = None
                    if loc == 0:
                        node.next = self.head
                        self.head = node
                    else:
                        while loc != 0:
                            prev_node = curr_node
                            curr_node = curr_node.next 
                            loc -= 1
                        prev_node.next = node
                        node.next = curr_node

    def delete(self, loc=-1):
        if loc >= self.size:
            raise ValueError("Index beyond Linked List bounds.")
        elif loc < -1:
            raise ValueError("Index cannot be less than -1.")
        else:
            self.size -= 1
            if loc == 0:
                k = self.head
                self.head = self.head.next
                del k
                if self.size == 0:
                    self.tail = None
            else:
                curr_node = self.head
                prev_node = None
                while loc != 0:
                    prev_node = curr_node
                    curr_node = curr_node.next 
                    loc -= 1
                prev_node.next = curr_node.next
                if curr_node == self.tail:
                    self.tail = prev_node
                del curr_node

    def get(self, ind):
        if ind >= self.size:
            raise ValueError("Index beyond Linked List bounds.")
        else:
            if ind == 0:
                return self.head.val
            elif ind == self.size - 1:
                return self.tail.val
            else:
                curr_node = self.head
                while ind != 0:
                    curr_node = curr_node.next
                    ind -= 1
                return curr_node.val

    def change(self, val, ind):
        if ind >= self.size:
            raise ValueError("Index beyond Linked List bounds.")
        else:
            if ind == 0:
                self.head.val = val
            elif ind == self.size - 1:
                self.tail.val = val
            else:
                curr_node = self.head
                while ind != 0:
                    curr_node = curr_node.next
                    ind -= 1
                curr_node.val = val
                    
    def reverse(self):
        curr_node = self.head
        prev_node = None
        self.tail = curr_node
        while curr_node.next != None:
            tmp_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp_node
        curr_node.next = prev_node
        self.head = curr_node

    def iterate(self):
        curr_node = self.head
        while curr_node != None:
            yield curr_node.val
            curr_node = curr_node.next
            
            

LL = LList()
for x in range(4):
    LL.insert(Node(x))

LL.insert(Node(-1),1)

for x in range(LL.size):
    print LL.get(x)

LL.reverse()
for x in range(LL.size):
    print LL.get(x)
print LL.tail.next
"""
for x in range(LL.size):
    LL.delete(0)
print LL.head, LL.tail
"""

print "Generator Function:"
for x in LL.iterate():
    print x

