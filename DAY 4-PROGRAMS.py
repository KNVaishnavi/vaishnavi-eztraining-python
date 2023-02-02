

'''d={n:n*n for n in range(1,5)}
print(d)'''

'''#CALCULATING PRODUCT PRICE FOR 5 UNITS
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)'''

'''#wITH CHECKS
real={'sam':24,'angel':18,'kumar':35}
now={name:age for(name,age) in real.items()if age>20}
print(now)'''

'''#create a list with 8 customer names display a dictionary which has customers names along with discounts for them from a particular shop
import random
l=["ali","ben","henry","peter","nody","tom","jerry","alen"]
d={names:random.randint(1,100) for names in l}
print(d)'''


'''l1=['a','b','c']
l2=[1,2,3]
d={a:b for(a,b) in zip(l1,l2)}
print(d)'''


'''import random
student_names=list(map(str,input("enter names:")))
marks=[]
for i in range(len(student_names)):
                   a=(random.randint(300,500)/500)*100
                   marks.append(a)
my_dict={x:y for(x,y) in zip(student_names,marks)}
print(my_dict)'''


'''n="hi i'am"sylvia""
SyntaxError: invalid syntax


n="hi i'am"
n
"hi i'am"


nm='hi i'am'
SyntaxError: unterminated string literal (detected at line 1)

m='hi i\'am'
m
"hi i'am"'''

'''#string operations
s=("apple")
s.upper()
'APPLE'
s.lower()
'apple'
s.capitalize()
'Apple'
s.replace('a','h')
'hpple'
s.strip()
'apple'
s1=("have a nice day")
s1.strip()
'have a nice day'
s1.split(',')
['have a nice day']
s.split(',')
['apple']
s.split('a')
['', 'pple']
s.center(31,'*')
'*************apple*************'
s.center(width,fillchar)
s.count('p')
2
s.count('p',3,len(s))
0
s.count('p',2,len(s))
1
s.endswith('e',0,len(s))
True
s.endswith('e',2,len(s))
True
s.find('a',0,len(s))
0
0
0
s.find('l',0,len(s))
3
s.index('e',2,len(s))
4

s=("apple")
s.islower()
True
s.isupper()
False
min(s)
'a'
max(s)
'p'
s.isupper()
False
s.istitle()
False
s.rfind('a',0,len(s))
0
s.rfind('p',0,len(s))
2


#mutable and immutable
X=20
X
20
x=30
x
30
id(x)
140722828994248
r=200
r=r+r
r
400
l=[2,3,4]
l.append(45)
l
[2, 3, 4, 45]



#get 1 string as input along with a character findout and display whether the character is present or not

s=input("enter a string:")
c=input("enter a char:")
if c in s:
    print("present")
else:
    print("not present")'''



'''s=input("enter:")
char=input()
for i in s:
    if i==char:
        flag=1
        break
    else:
     flag=0
if flag==1:
        print("present")
else:
        print("not present")'''


'''st= input("enter the sting:")
ch= input("enter char:")
a="yes" if ch in st else "no"
print(a)'''

'''
#check whether the given string is palindrome or not
str1=input("enter:")
if (str1==str1[::-1]):
    print("is palindrome")
else:
    print("not a palindrome")'''




    
'''#after getting the string chech whether the string contains space or not
s=input("enter:")
count=0
for i in s:
    if i==" ":
        count+=1
print(count)'''

'''
#create a list with vowels get one string as input, count vowel from the string and display the result
l=["a","e","i","o","u"]
n=input("enter a string")
count=0
for i in n:
    if i in l:
        count+=1
print(count)
'''

#MATH MODULE
import math
print("ceil 12.5:",math.ceil(12.5))
print("floor 12.5",math.floor(12.5))
print("sqrt 345:",math.sqrt(345))
print("factorial 3:",math.factorial(3))
print("powe 2,3:",math.pow(2,3))
print("remainder 10,3:",math.fmod(10,3))
a,b=divmod(10,3)
print(a,b)













