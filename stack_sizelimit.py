# with size Limit

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # Is Empty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #Is Full    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    #Push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "Element Successfully added"
        
    #Pop
    def pop(self):
        if self.isEmpty():
            return "There is no element in the list"
        else:
            return self.list.pop()

    #Peek
    def peek(self):
        if self.isEmpty():
            return "There is no Element"
        else:
            return self.list[len(self.list)-1]

    #delete
    def delete(self):
        self.list = None            
        

customStack1 = Stack(4)  
print(customStack1.isEmpty()) 
print(customStack1.isFull())    
customStack1.push(1) 
customStack1.push(2)    
customStack1.push(3)   
print(customStack1)

