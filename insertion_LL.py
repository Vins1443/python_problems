class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next 
    # Insert in LL
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode 

SinglyLinkedList = SLinkedList()
SinglyLinkedList.insertSLL(1, 1)
SinglyLinkedList.insertSLL(2, 1)
SinglyLinkedList.insertSLL(3, 1)
SinglyLinkedList.insertSLL(4, 1)

SinglyLinkedList.insertSLL(0, 0)
SinglyLinkedList.insertSLL(68, 4)



print([node.value for node in SinglyLinkedList])
