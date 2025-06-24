# creating stack datastructure -by using LifoQueue class from queue module

from queue import LifoQueue
st=LifoQueue(maxsize=4)    #Initializing a stack
# put() function to push
print("SIZE:", st.qsize())
st.put('a')
st.put('b')
st.put('c')
st.put('d')

print("SIZE:", st.qsize())
print("FULL:", st.full())
'''
print('\n Elements popped from the stack')
print(st.get())
print(st.get())
print(st.get())
print(st.get())
'''
# get() function to pop
st.get()
print("SIZE:",st.qsize())
st.get()
print("SIZE:",st.qsize())
st.get()
print("SIZE:",st.qsize())
st.get()
print("SIZE:",st.qsize())
print("\nEMPTY:", st.empty())
