from collections import deque
import queue as q
from multiprocessing import Queue

customQueue = deque(maxlen=3)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)

print(customQueue)

customQueue1 = q.Queue(maxsize=3)
customQueue1.put(1)
customQueue1.put(56)
customQueue1.put(16)

print(customQueue1.full())

customQueue2 = Queue(maxsize=3)
customQueue2.put(4)
print(customQueue2.get())
print(customQueue1.get())