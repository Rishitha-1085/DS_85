# deque- DOUBLE ENDED QUEUE

from collections import deque
dq=deque(['mon','tue','wed'])
print(dq)
# INSERTING DATA ON BOTH SIDES
dq.append('thus')      #append_right
print(dq)
dq.appendleft('sun')      
print(dq)
# DELETING DATA ON BOTH SIDES
dq.pop()
print(dq)
dq.popleft()
print(dq)