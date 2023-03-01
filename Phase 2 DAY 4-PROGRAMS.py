
'''#STACK IS LIFO-LAST IN FIRST OUT
stack=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("removed element",e)
        print(stack)

while True:
    print("select operation 1.push 2.pop 3.exit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("select a valid operation")
        


#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode=self.head
            self.head=self.head.next
            poppednode.next=None
            return poppednode.data
    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data
    def display(self):
        t=self.head
        if self.isempty():
            print("stack underflow")
        else:
            while(t!= None):
                print(t.data,end="")
                t=t.next
                if(t!=None):
                    print("->",end="")
            return
if __name__=="__main__":
    S=Stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.display()
    print(S.peek())
    S.pop()
    S.pop()
    S.display()
    

#
s=input()
st=[]
balanced=True
for char in s:
    if (char=='{' or char=='[' or char=='('):
        st.append(char)
    elif(char=='}'):
        if(len(st)and st.pop()!='{'):
            balanced=False
            break
    elif(char==']'):
        if(len(st)and st.pop()!='['):
            balanced=False
            break
    elif(char==')'):
        if(len(st)and st.pop()!='('):
            balanced=False
            break
    else:
        balanced=False
        break
if(balanced==False or len(st)):
    print("not balanced")
else:
    print("balanced")


#QUEUE
queue=[]
def enqueue():
    element=int(input("enter element"))
    queue.append(element)
    print(element,"is added in q")

def dequeue():
    if not queue:
        print("Q is empty")
    else:
        e=queue.pop(0)
        print("removed element",e)

def display():
    print(queue)

while True:
    print("select operation 1.add,2.remove,3.show")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("enter valid operation")
        break


#
from queue import LifoQueue
s=LifoQueue(maxsize=3)
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())


#implementation of queue using queue module
import queue
l=queue.Queue(maxsize=5)
l.put(10)
l.put(20)
print(l.get())
print(l.get())


#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
        self.last=None

    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return=self.head.data
            self.head=self.head.next
            return to_return

q_queue=Queue()
while True:
    print('enqueue<value>')
    print('dequeue')
    print('quit')
    do=input('what would you like to do?').split()
    operation=do[0].strip().lower()
    if operation=='enqueue':
        q_queue.enqueue(int(do[1]))
    elif operation=='dequeue':
        dequeued=q_queue.dequeue()
        if dequeued is None:
            print('queue is empty')
        else:
            print('dequeued element:',int(dequeued))
    elif operation  =='quit':
        break
            
'''
#
class Node:
    def __init__(self,data):
        self.data=data
        self.node=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None

    def append(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def get_prev_node(self,ref_node):
        current=self.head
        while(current and current.next!=ref_node):
            current=current.next
        return current
    def remove(self,node):
        prev_node=self.get_prev_node(node)
        if prev_node is None:
            self.head=self.head.next
        else:
            prev_node.next=node.next
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
    def remove_duplicates(llist):
        current1=llist.head
        while current1:
            data=current1.data
            current2=current1.next
        while current2:
            if current2.data==data:
                llist.remove(current2)
                current2=current2.next
                current1=current1.next

a_llist=LinkedList()
data_list=input('please enter the elements in the linked list:').split()
for data in data_list:
    a_llist.append(int(data))
remove_duplicates(a_llist)
print('the list with duplicates removed:')
a_llist.display()
    
