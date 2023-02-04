

#
q1="""who is the first prime minister of India?
a. Narendra Modi
b. Jawaharlala Nehuru
c. Subhash Chandra Bose
d. Gandhi"""
q2="""what is the the double standard structure?
a. DNA
b. RNA
c. chromoplast
d. mesosomes"""
q3="""who invented zero?
a. Arya Batta
b. C V Ramanujan
c. Rome
d. Nikhil"""
q4="""A doctor who treats eye related issues is known as?
a. Orthopedic
b. Opthomalagist
c. Endocrinology
d. Pulmonology"""
q5="""what is the famous temple present in konark?
a. Sun temple
b. Isckon temple
c. Durga temple
d. Kali temple"""

questions={q1:"b",q2:"a",q3:"a",q4:"b",q5:"a"}

name=input("hi what is your name")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this question (yes/no)")
    if flag1=='yes':
                continue
    ans=input("enter your answer")
    if ans== questions[i]:
        print("wow! you got one point")
        score+=1
        print("your current score is:",score)
    else:
        print("wrong answer, you lost 1 point")
        score-=1
        print("your current score is:",score)
    flag2=input("do you want to quit? type(yes/no)")
    if flag2=="yes":
        break
print("your total score is:",score)




                        
