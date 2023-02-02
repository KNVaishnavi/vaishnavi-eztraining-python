
#NUM GAME
import random
n= random.randrange(1,50)
guess= int(input("enter any number:"))
while n!=guess:
    if guess < n:
        print("too low")
        guess= int(input("enter number again:"))
    elif guess > n:
        print("too high")
        guess= int(input("enter number again:"))
    else:
        break
print("you guessed it right!!")
        

#CONDITIONAL LOOPS     
n=2
while (n<=20):
    if(n%2==0):
        print(n)
    n=n+1

n=1
while (n<=20):
    if(n%2!=0):
        print(n)
    n=n+1

for i in range(1,11):
    print(i)


for i in range(2,11,2):
    print(i)


for i in range(1,20):
    if(i%2==0):
        print(i)

        
n=1
while n<=10:
    print(n)
    n=n+1

n=1
if type(n)==int:
    print("the number is integer")
elif type(n)==float:
     print("the number is float")
else:
    print("the number is other data type")


    
n=1
if(n%1==0):
    print("the number is integer")
else:
     print("the number is float")
    


n=2.9
if n==int(n):
    print("the number is integer")
elif n==float(n):
    print("the number is float")



n=2
if isinstance(n,float)==True:
    print("the number is float")
else:
    print("the number is integer")


#INT OR FLOAT
n=10.3
res=n-int(n)
if res>0 or res!=0:
    print("float")
else:
    print("integer")

    

#COMPARING 2 NUMBERS
    a,b=int(input("enter a:")),int(input("enter b:"))
if(a>b):
    print("a is big:",a)
else:
    print("b is big:",b)



#EVEN OR ODD
    n=int(input("enter number:"))
if (n<0)&(n%2==0):
    print("the number is negative and even")
elif (n>0)&(n%2==0):
    print("the number is positive and even")
elif (n<0)&(n%2!=0):
    print("the number is negative and odd")
else:
    print("the number is positive and odd")



#NUMBER IS 500
n=int(input("enter number:"))
if n==500:
    print("given number is 500")
else:
    print("given number is not 500") 


