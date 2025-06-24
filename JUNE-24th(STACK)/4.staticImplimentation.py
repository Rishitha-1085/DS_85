# creating stack datastructure -by using LifoQueue class from queue module
# static Implimentation -using LifoQueue,deque

from queue import LifoQueue
st=LifoQueue(maxsize=4)   
st.put('a')
st.put('b')
st.put('c')
st.put('d')
print("SIZE:", st.qsize())
print("FULL:", st.full())
print('\nElements popped from the stack')
print(st.get())
print(st.get())
print(st.get())
print(st.get())
print("SIZE:", st.qsize())