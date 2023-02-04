'''import random as r
x="i love sweets"
print(r.sample(x,2))
['l', 'o']'''

'''#everytime it gives different output
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)
[5, 2, 4, 6, 3, 1]
a=[1,2,3,4,5,6]
print(r.choice(a))
4
b="welcome back"
print(r.choice(b))
e
a=r.random
a=r.random()
print(a)
0.9174120651664234

#will return randon number between 0.0 to 1.0
#0.0 includes 1.0 excludes
print(r.randint(20,30))
27
a=[10,20,30,40,50]
print(r.choices(a,k=10))
[30, 10, 30, 30, 50, 10, 10, 40, 10, 10]
print(r.choices(a,n=9))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(r.choices(a,n=9))
TypeError: Random.choices() got an unexpected keyword argument 'n'
s="hello good day"
print(r.choices(s,k=9))
['h', 'o', 'h', 'o', 'o', 'l', 'd', ' ', 'o']
print(r.uniform(5,10))
8.283134579938444


#finding different functions present
z=dir(r)
print(z)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

#calender
import calendar
print("full calendar")
full calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

print(calendar.month(2021,3))
     March 2021
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31

print("set first day of the week")
set first day of the week
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2021,12))
   December 2021
Fr Sa Su Mo Tu We Th
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31


#time module
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
fv=a.strftime("%Y")
print("year shor version",sv)
print("yera full version",fv)


#without arg and without return
def sample():
    print("great day")
    print("happy time")
sample()
print("today")
sample()

def multi():
    n1=int(input("enter num:"))
    n2=int(input("enter num:"))
    n3=int(input("enter num:"))
    prod=n1*n2*n3
    print(prod)
multi()

#with return and without arg
def multi():
    n1=int(input("enter num:"))
    n2=int(input("enter num:"))
    n3=int(input("enter num:"))
    prod=n1*n2*n3
    return prod
res=multi()
print(res)


#with arg and witout return
def multi(n1,n2,n3):
    prod=n1*n2*n3
    print(prod)

def multi(a,b,c):
    prod=a*b*c
    print(prod)
n1=int(input("enter num:"))
n2=int(input("enter num:"))
n3=int(input("enter num:"))
multi(n1,n2,n3)

#with arg and with return

def multi(n1,n2,n3):
    prod=n1*n2*n3
    return prod
res=multi(3,4,5)
print (res)

def multi(a,b,c):
    prod=a*b*c
    return prod
n1=int(input("enter num:"))
n2=int(input("enter num:"))
n3=int(input("enter num:"))
res=multi(n1,n2,n3)
print(res)


#lemons program usiong fun type 1
#find factors of the given num using func type 2
#print multiplication table of the given num usong fun type 3
#find out sum of digits of the given num using fun type 4


def lemons():
    a=int(input("enter num:"))
    b=int(input("enter num:"))
    c=int(input("enter num:"))
    s=0
    s=a+b+c
    print(s)

    if (s>21):
        print("lemons exceede",s-21)
    elif (s<21):
        print("lemons not sufficient",21-s)
    else:
        print("lemons required are sufficient")
lemons()


#
def multi_table(n):
    for i in range(1,11):
        print(i,"x",n,"=",i*n)
n=int(input("which table:"))
multi_table(n)    

#
n=int(input("number:"))
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            

#
def digits(n):
    sum=0
    while n!=0:
        rem=n%10
        sum=sum+rem
        n=n//10
    return sum
n=int(input("enter the number"))
res=digits(n)
print(res)


#
def display():
    n=int(input("enter a number"))
    if n==1:
    display()
    else:
        print("over")
display()'''

#Factorial
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
result=fact(5)
print(result)          //1*1=1,2*1=2,3*2=6,4*6=24,5*24=120
                         

#
n=int(input("enter number:")
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end=" ")
    count+=1
    a=b
    b=sum
    sum=a+b


#function returns more values
#addition and subtraction  in one function 
def add_sub(x,y):
    sub=x-y
    add=x+y
    return sub,add
res1,res2=add_sub(20,10)
print(res1)
print(res2)


#varible length method
def summ(*a):
    c=0
    for i in a:
        c=c+i
    print(c)
summ(10,2,3,1,2)
