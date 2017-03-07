from Node import Node
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def put(self,value):
        tmp_node = Node(value,None)
        if self.head is None:
            self.head = tmp_node
            self.tail = tmp_node
        else :
            self.tail.setNext(tmp_node)
            self.tail = self.tail.getNext()

    def pop(self):
        if self.head is None:
            self.tail = None
            return None
        else:
            tmp_val = self.head.getValue()
            self.head = self.head.getNext()
            return tmp_val

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.getValue()




