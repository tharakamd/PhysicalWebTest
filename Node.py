class Node:


    def __init__(self,value,next):
        self.value = value
        self.next = next

    def setNext(self,next):
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next