'''
#
a=100
b=0
try:
    print(a/b)
except Exception as e:
    print("please note number cant be divided by zero",e)
print("bye")



#

a=10
b=2
try:
    print("resource open")
    print(a/b)
except Exception as e:
    print("dont give second num as zero",e)
finally:
    print("resource closed")

#
a=10
try:
    b=int(input("enter the number"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note,number cant be divided by zero",e)
except ValueError as e:
    print("invalid input",e)
except exception as e:
    print("other error")
finally:
    print("resource closed")
    

#
x=109
if x%2!=0:
    raise Exception("x should be even number")
else:
    print("x is even number...correct")

    
#
class computer:
     def config(self):
         print("yes")
lenova=computer()
lenova.config()
dell=computer()
dell.config()


#constructor
class Employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name
    def display(self):
        print("id:%d \n name:%s" % (self.id,self.name))
emp1=Employee("john",101)
emp2=Employee("david",102)
emp1.display()
emp2.display()
'''

#variables and var.access in class and method
class computer():
    a=10
    b=20
    print("class variables inside class:",a)
    def config(self):
        c=100
        print("yes")
        print("instance access",self.b)
lenova=computer()
print(lenova.a)
print(lenova.a+lenova.b)
dell=computer()
print("dell",dell.a)
lenova.config()
               
