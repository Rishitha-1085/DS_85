# SIMPLE QUEUE/ LINEAR QUEUE:
# IMPLIMENTATION - using collections module -deque class

from collections import deque
lq=deque(maxlen=4)    #lq-linearqueue
lq.append(10)
print(lq)
lq.append(20)
print(lq)
lq.append(30)
print(lq)
lq.append(40)
print(lq)
lq.append(50)    # 10 data is deleted and 50 is added 
print(lq)
# DELETION:
lq.popleft()
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)
lq.popleft()
print(lq)