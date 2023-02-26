HAPPY NUM IS 1 IF THE SQUARE OF THE DIGITS AND AGAIN ITS DIGITS IS 1
def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
                       r=n%10
                       s=s+r**2
                       n=n//10
        return s
n=int(input("enter the num:"))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("happy number")
else:
    print("not a happy number")
    

#protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()


#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)



#METHOD OVERLOADING
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("with all arguments")
obj.display(20,30)
print("with one argument")
obj.display(10)

#
class vijayawada():
    def placename(self):
        print("vijayawada placename is KLU")
    def student(self):
        print("yes-vijayawada")
    def which_year(self):
        print("3rd year")
class hyd():
     def placename(self):
        print("hyd placename is hyd-KLU")
     def student(self):
         print("yes-hyd")
     def which_year(self):
         print("3rd year-hyd")
obj_vij=vijayawada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placename()
    details.student()
    details.which_year()

#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
obj.display()




#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.display()


#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(20)
n1.next=n2
n3=Node(20)
n2.next=n3
n4=Node(20)
n3.next=n4
print("before inserting100")
obj.display()
print(" ")
print("after inserting 100")
obj.insert_beginning(100)
obj.display()
print(" ")
print("after inserting 555")
obj.insert_beginning(555)
obj.display()



#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(20)
n1.next=n2
n3=Node(20)
n2.next=n3
n4=Node(20)
n3.next=n4
obj.insert_end(111111)
obj.display()



#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
        
def insert_position(self,pos,data):
    np=Node(data)
    temp=self.head
    for i in range(pos-1):
        temp=temp.next
    np.next=temp.next
    temp.next=np
    
def display(self):
    if self.head is None:
        print("linked list is empty")
    else:
        temp=self.head
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next





#
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
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
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
a_llist=LinkedList()
n=int(input('how many elements would you like to insert'))
for i in range(n):
    data=int(input('enter the data item:'))
    a_llist.append(data)
print('the linked list: ',end=' ')
a_llist.display()

