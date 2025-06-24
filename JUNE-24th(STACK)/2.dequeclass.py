# creating stack datastructure -by using deque class from collections module
# EG: static Implimentation
from collections import deque
st=deque(maxlen=4)   #size is fixed-4
st.append(10)
st.append(20)
st.append(30)
st.append(40)
print(st)
st.append(50)  # first data(ie 10) is removes because size is fixed ie 4 
print(st)

# pop operation
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)
st.pop()
print(st)