myList = list()
while(True):
    inp = input('enter a number')
    if inp == 'done':break
    value = float(inp)
    myList.append(value)

    average = sum(myList)/len(myList)

print('Average', average)    

