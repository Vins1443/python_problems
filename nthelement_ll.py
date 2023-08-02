from LL_interview import LinkedList

def nthToLast(ll,n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customll1 = LinkedList()   
customll1.generate(10, 0, 99)
print(customll1)
print(nthToLast(customll1,3))
