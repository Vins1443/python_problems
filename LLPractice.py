class linkedNodes:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

node1 = linkedNodes("3") 
node2 = linkedNodes("7")
node3 = linkedNodes('10')

node1.nextNode = node2
node2.nextNode = node3

currentNode = node1
while True:
    print(currentNode.value, "->",)
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode

